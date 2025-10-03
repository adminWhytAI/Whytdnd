"""
Immersive Parser - Parses first-person immersive documentation
Extracts narrative fragments from "Being_A_X" and "Having_X" files
"""
import re
from pathlib import Path
from typing import Dict, List, Optional
import hashlib

from backend.utils.logger import logger
from backend.utils.exceptions import ConfigurationError


class ImmersiveDocParser:
    """
    Parses immersive documentation files to extract first-person narrative fragments
    """
    
    def __init__(self, immersive_dir: Path):
        """
        Args:
            immersive_dir: Path to Documentation/Immersive directory
        """
        self.immersive_dir = immersive_dir
        self.races_dir = immersive_dir / "Races"
        self.classes_dir = immersive_dir / "Classes"
        self.stats_dir = immersive_dir / "Stats"
        self.alignments_dir = immersive_dir / "Alignments"
        
    def parse_all_immersive_docs(self) -> Dict[str, List[Dict]]:
        """
        Parse all immersive documentation files
        
        Returns:
            Dict with categories (races, classes, stats, alignments) mapping to fragments
        """
        logger.info("Parsing all immersive documentation")
        
        result = {
            'races': [],
            'classes': [],
            'stats': [],
            'alignments': []
        }
        
        # Parse each category
        if self.races_dir.exists():
            result['races'] = self._parse_directory(self.races_dir, 'race')
            
        if self.classes_dir.exists():
            result['classes'] = self._parse_directory(self.classes_dir, 'class')
            
        if self.stats_dir.exists():
            result['stats'] = self._parse_directory(self.stats_dir, 'stat')
            
        if self.alignments_dir.exists():
            result['alignments'] = self._parse_directory(self.alignments_dir, 'alignment')
        
        total_fragments = sum(len(v) for v in result.values())
        logger.info(f"Parsed {total_fragments} total fragments from immersive docs")
        
        return result
    
    def _parse_directory(self, directory: Path, category: str) -> List[Dict]:
        """
        Parse all markdown files in a directory
        
        Args:
            directory: Directory containing markdown files
            category: Category type (race, class, stat, alignment)
            
        Returns:
            List of fragment dictionaries
        """
        fragments = []
        
        for md_file in directory.glob("*.md"):
            try:
                file_fragments = self.parse_file(md_file, category)
                fragments.extend(file_fragments)
                logger.info(f"Parsed {len(file_fragments)} fragments from {md_file.name}")
            except Exception as e:
                logger.error(f"Error parsing {md_file}: {e}")
        
        return fragments
    
    def parse_file(self, filepath: Path, category: str) -> List[Dict]:
        """
        Parse a single immersive documentation file
        
        Args:
            filepath: Path to markdown file
            category: Category type
            
        Returns:
            List of fragment dictionaries
        """
        logger.debug(f"Parsing immersive file: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata from filename
        metadata = self._extract_metadata_from_filename(filepath.stem, category)
        
        # Split content into sections
        sections = self._split_into_sections(content)
        
        # Create fragments
        fragments = []
        for section_title, section_content in sections.items():
            fragment = self._create_fragment(
                section_title,
                section_content,
                metadata,
                category
            )
            fragments.append(fragment)
        
        return fragments
    
    def _extract_metadata_from_filename(self, filename: str, category: str) -> Dict:
        """
        Extract metadata from filename
        
        Examples:
            Being_A_Dwarf_Mountain -> race: Dwarf Mountain
            Being_A_Fighter -> class: Fighter
            Having_High_Strength -> stat: Strength (high)
            Living_Lawful_Good -> alignment: Lawful Good
        
        Args:
            filename: Filename without extension
            category: Category type
            
        Returns:
            Metadata dictionary
        """
        metadata = {'category': category}
        
        if category == 'race':
            # Being_A_Dwarf_Mountain -> Dwarf Mountain
            name = filename.replace('Being_A_', '').replace('_', ' ')
            metadata['race'] = name
            
        elif category == 'class':
            # Being_A_Fighter -> Fighter
            name = filename.replace('Being_A_', '').replace('_', ' ')
            metadata['class'] = name
            
        elif category == 'stat':
            # Having_High_Strength -> Strength, high
            parts = filename.replace('Having_', '').split('_')
            if len(parts) >= 2:
                level = parts[0].lower()  # high, low, average
                stat = '_'.join(parts[1:]).replace('_', ' ')
                metadata['stat'] = stat
                metadata['level'] = level
                
        elif category == 'alignment':
            # Living_Lawful_Good -> Lawful Good
            name = filename.replace('Living_', '').replace('_', ' ')
            metadata['alignment'] = name
        
        return metadata
    
    def _split_into_sections(self, content: str) -> Dict[str, str]:
        """
        Split markdown content into sections based on headers
        
        Args:
            content: Full markdown content
            
        Returns:
            Dict mapping section titles to content
        """
        sections = {}
        
        # Split on ## headers (h2)
        parts = re.split(r'\n## (.+?)\n', content)
        
        # First part is before any header (title, intro)
        if parts[0].strip():
            sections['Introduction'] = parts[0].strip()
        
        # Process header/content pairs
        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                section_title = parts[i].strip()
                section_content = parts[i + 1].strip()
                sections[section_title] = section_content
        
        return sections
    
    def _create_fragment(
        self, 
        section_title: str, 
        section_content: str, 
        metadata: Dict,
        category: str
    ) -> Dict:
        """
        Create a knowledge fragment from a section
        
        Args:
            section_title: Title of the section
            section_content: Content of the section
            metadata: File metadata
            category: Category type
            
        Returns:
            Fragment dictionary ready for vectorization
        """
        # Generate unique ID
        fragment_id = self._generate_fragment_id(
            metadata,
            section_title,
            section_content
        )
        
        # Extract key phrases (sentences with "I", "my", etc.)
        first_person_content = self._extract_first_person_content(section_content)
        
        fragment = {
            'id': fragment_id,
            'category': category,
            'metadata': metadata,
            'section_title': section_title,
            'content': section_content,
            'first_person_excerpts': first_person_content,
            'word_count': len(section_content.split()),
            'type': 'immersive_narrative'
        }
        
        return fragment
    
    def _generate_fragment_id(self, metadata: Dict, section: str, content: str) -> str:
        """
        Generate unique fragment ID
        
        Args:
            metadata: Fragment metadata
            section: Section title
            content: Section content
            
        Returns:
            Unique hash-based ID
        """
        # Create string to hash
        id_string = f"{metadata}_{section}_{content[:100]}"
        hash_obj = hashlib.md5(id_string.encode())
        return hash_obj.hexdigest()[:12]
    
    def _extract_first_person_content(self, content: str) -> List[str]:
        """
        Extract sentences with strong first-person perspective
        
        Args:
            content: Section content
            
        Returns:
            List of first-person sentences
        """
        # Split into sentences
        sentences = re.split(r'[.!?]\s+', content)
        
        # Filter for first-person markers
        first_person_markers = [
            r'\bI\b', r'\bmy\b', r'\bme\b', r'\bmine\b',
            r'\bmyself\b', r'\bI\'m\b', r'\bI\'ve\b', r'\bI\'ll\b'
        ]
        
        pattern = '|'.join(first_person_markers)
        
        first_person_sentences = [
            sent.strip() + '.'
            for sent in sentences
            if re.search(pattern, sent, re.IGNORECASE) and len(sent.strip()) > 20
        ]
        
        return first_person_sentences[:5]  # Top 5 most relevant


class FragmentExtractor:
    """
    Extracts and processes knowledge fragments for RAG
    """
    
    def __init__(self, parser: ImmersiveDocParser):
        """
        Args:
            parser: ImmersiveDocParser instance
        """
        self.parser = parser
        
    def extract_fragments_by_type(self, fragment_type: str) -> List[Dict]:
        """
        Extract fragments of a specific type
        
        Args:
            fragment_type: Type (race, class, stat, alignment)
            
        Returns:
            List of fragments
        """
        all_fragments = self.parser.parse_all_immersive_docs()
        return all_fragments.get(fragment_type, [])
    
    def extract_fragments_for_character(self, character_data: Dict) -> List[Dict]:
        """
        Extract relevant fragments for a specific character
        
        Args:
            character_data: Character information (race, class, stats, alignment)
            
        Returns:
            List of relevant fragments
        """
        fragments = []
        
        all_docs = self.parser.parse_all_immersive_docs()
        
        # Get race fragments
        if 'race' in character_data:
            race_name = character_data['race']
            for fragment in all_docs['races']:
                if fragment['metadata'].get('race', '').lower() == race_name.lower():
                    fragments.append(fragment)
        
        # Get class fragments
        if 'class' in character_data:
            class_name = character_data['class']
            for fragment in all_docs['classes']:
                if fragment['metadata'].get('class', '').lower() == class_name.lower():
                    fragments.append(fragment)
        
        # Get stat fragments based on ability scores
        if 'abilities' in character_data:
            for ability, score in character_data['abilities'].items():
                level = self._categorize_stat_level(score)
                for fragment in all_docs['stats']:
                    if (fragment['metadata'].get('stat', '').lower() == ability.lower() and
                        fragment['metadata'].get('level') == level):
                        fragments.append(fragment)
        
        # Get alignment fragments
        if 'alignment' in character_data:
            alignment = character_data['alignment']
            for fragment in all_docs['alignments']:
                if fragment['metadata'].get('alignment', '').lower() == alignment.lower():
                    fragments.append(fragment)
        
        return fragments
    
    def _categorize_stat_level(self, score: int) -> str:
        """
        Categorize ability score into level
        
        Args:
            score: Ability score value
            
        Returns:
            Level category (high, average, low)
        """
        if score >= 16:
            return 'high'
        elif score <= 9:
            return 'low'
        else:
            return 'average'


if __name__ == "__main__":
    # Test the parser
    from backend.utils.config import DOCUMENTATION_DIR
    
    print("="*60)
    print("TESTING IMMERSIVE PARSER")
    print("="*60)
    
    immersive_dir = DOCUMENTATION_DIR / "Immersive"
    
    if not immersive_dir.exists():
        print(f"⚠️  Immersive directory not found: {immersive_dir}")
    else:
        parser = ImmersiveDocParser(immersive_dir)
        all_fragments = parser.parse_all_immersive_docs()
        
        print(f"\n✅ Parsed immersive documentation:")
        print(f"   Races: {len(all_fragments['races'])} fragments")
        print(f"   Classes: {len(all_fragments['classes'])} fragments")
        print(f"   Stats: {len(all_fragments['stats'])} fragments")
        print(f"   Alignments: {len(all_fragments['alignments'])} fragments")
        
        # Show sample fragment
        if all_fragments['races']:
            print("\n📋 Sample Race Fragment:")
            sample = all_fragments['races'][0]
            print(f"   ID: {sample['id']}")
            print(f"   Section: {sample['section_title']}")
            print(f"   Metadata: {sample['metadata']}")
            print(f"   First-person excerpts: {len(sample['first_person_excerpts'])}")
