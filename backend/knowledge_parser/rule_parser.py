"""
Rule Parser - Parses technical D&D 5e documentation
Extracts races, classes, and game mechanics from markdown files
"""
import re
from pathlib import Path
from typing import Dict, List, Optional
import markdown
from bs4 import BeautifulSoup

from backend.utils.logger import logger
from backend.utils.exceptions import ConfigurationError


class RaceParser:
    """
    Parses race documentation to extract mechanical information
    """
    
    def __init__(self, documentation_dir: Path):
        """
        Args:
            documentation_dir: Path to Documentation/Technical directory
        """
        self.documentation_dir = documentation_dir
        self.races_file = documentation_dir / "02_Races.md"
        
    def parse_races(self) -> Dict[str, Dict]:
        """
        Parse all races from the races documentation file
        
        Returns:
            Dict mapping race names to their attributes
        """
        if not self.races_file.exists():
            raise ConfigurationError(f"Races file not found: {self.races_file}")
        
        logger.info(f"Parsing races from {self.races_file}")
        
        with open(self.races_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown to HTML for easier parsing
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        
        races = {}
        current_race = None
        current_subrace = None
        
        # Parse structure (this is a simplified example - adjust based on actual markdown structure)
        for heading in soup.find_all(['h2', 'h3', 'h4']):
            text = heading.get_text().strip()
            
            if heading.name == 'h2' and not text.startswith('Tableau'):
                # Main race
                current_race = {
                    'name': text,
                    'subraces': {},
                    'traits': [],
                    'ability_score_increase': {},
                    'size': None,
                    'speed': None,
                    'languages': []
                }
                races[text] = current_race
                current_subrace = None
                
            elif heading.name == 'h3' and current_race:
                # Could be subrace or trait section
                if 'Sous-race' in text or 'Subrace' in text:
                    current_subrace = text
                    current_race['subraces'][text] = {
                        'traits': [],
                        'ability_score_increase': {}
                    }
        
        return races
    
    def extract_ability_scores(self, text: str) -> Dict[str, int]:
        """
        Extract ability score increases from text
        
        Args:
            text: Text containing ability score information
            
        Returns:
            Dict mapping ability names to bonuses
        """
        abilities = {}
        
        # Pattern: "+2 Force", "+1 Dextérité", etc.
        pattern = r'\+(\d+)\s+(Force|Dextérité|Constitution|Intelligence|Sagesse|Charisme|Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma)'
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        # Map French to English
        ability_map = {
            'Force': 'Strength',
            'Dextérité': 'Dexterity', 
            'Constitution': 'Constitution',
            'Intelligence': 'Intelligence',
            'Sagesse': 'Wisdom',
            'Charisme': 'Charisma'
        }
        
        for bonus, ability in matches:
            english_ability = ability_map.get(ability, ability)
            abilities[english_ability] = int(bonus)
        
        return abilities


class ClassParser:
    """
    Parses class documentation to extract mechanical information
    """
    
    def __init__(self, documentation_dir: Path):
        """
        Args:
            documentation_dir: Path to Documentation/Technical directory
        """
        self.documentation_dir = documentation_dir
        self.classes_file = documentation_dir / "03_Classes_Resume.md"
        
    def parse_classes(self) -> Dict[str, Dict]:
        """
        Parse all classes from the classes documentation file
        
        Returns:
            Dict mapping class names to their attributes
        """
        if not self.classes_file.exists():
            raise ConfigurationError(f"Classes file not found: {self.classes_file}")
        
        logger.info(f"Parsing classes from {self.classes_file}")
        
        with open(self.classes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        
        classes = {}
        current_class = None
        
        for heading in soup.find_all(['h2', 'h3']):
            text = heading.get_text().strip()
            
            if heading.name == 'h2':
                # Main class
                current_class = {
                    'name': text,
                    'hit_die': None,
                    'primary_ability': [],
                    'saving_throws': [],
                    'armor_proficiencies': [],
                    'weapon_proficiencies': [],
                    'tool_proficiencies': [],
                    'skills': [],
                    'features': []
                }
                classes[text] = current_class
        
        return classes
    
    def extract_hit_die(self, text: str) -> Optional[int]:
        """
        Extract hit die from text
        
        Args:
            text: Text containing hit die information
            
        Returns:
            Hit die value (e.g., 6, 8, 10, 12) or None
        """
        pattern = r'd(\d+)'
        match = re.search(pattern, text)
        return int(match.group(1)) if match else None


class RuleExtractor:
    """
    High-level interface for extracting D&D rules from documentation
    """
    
    def __init__(self, documentation_dir: Path):
        """
        Args:
            documentation_dir: Path to Documentation/Technical directory
        """
        self.documentation_dir = documentation_dir
        self.race_parser = RaceParser(documentation_dir)
        self.class_parser = ClassParser(documentation_dir)
        
    def extract_all_rules(self) -> Dict:
        """
        Extract all rules (races, classes, etc.) from documentation
        
        Returns:
            Comprehensive rules database
        """
        logger.info("Starting full rules extraction")
        
        rules = {
            'races': {},
            'classes': {},
            'version': '5e',
            'source': 'D&D 5e SRD'
        }
        
        try:
            rules['races'] = self.race_parser.parse_races()
            logger.info(f"Extracted {len(rules['races'])} races")
        except Exception as e:
            logger.error(f"Error parsing races: {e}")
            rules['races'] = {}
        
        try:
            rules['classes'] = self.class_parser.parse_classes()
            logger.info(f"Extracted {len(rules['classes'])} classes")
        except Exception as e:
            logger.error(f"Error parsing classes: {e}")
            rules['classes'] = {}
        
        return rules


def parse_races_from_md(filepath: Path) -> Dict[str, Dict]:
    """
    Convenience function to parse races from a markdown file
    
    Args:
        filepath: Path to races markdown file
        
    Returns:
        Dict of races
    """
    parser = RaceParser(filepath.parent)
    return parser.parse_races()


def parse_classes_from_md(filepath: Path) -> Dict[str, Dict]:
    """
    Convenience function to parse classes from a markdown file
    
    Args:
        filepath: Path to classes markdown file
        
    Returns:
        Dict of classes
    """
    parser = ClassParser(filepath.parent)
    return parser.parse_classes()


if __name__ == "__main__":
    # Test the parser
    from backend.utils.config import DOCUMENTATION_DIR
    
    print("="*60)
    print("TESTING RULE PARSER")
    print("="*60)
    
    technical_docs = DOCUMENTATION_DIR
    
    extractor = RuleExtractor(technical_docs)
    rules = extractor.extract_all_rules()
    
    print(f"\n✅ Extracted {len(rules['races'])} races")
    print(f"✅ Extracted {len(rules['classes'])} classes")
    
    print("\n📋 Sample Race:")
    if rules['races']:
        first_race = list(rules['races'].keys())[0]
        print(f"  {first_race}: {rules['races'][first_race]}")
    
    print("\n📋 Sample Class:")
    if rules['classes']:
        first_class = list(rules['classes'].keys())[0]
        print(f"  {first_class}: {rules['classes'][first_class]}")
