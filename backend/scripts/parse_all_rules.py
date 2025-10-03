"""
Parse All Rules - Generate comprehensive rules database from documentation
Runs parsers and creates data/rules_database.json
"""
import sys
import json
from pathlib import Path
from datetime import datetime

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from knowledge_parser.rule_parser import RuleExtractor
from knowledge_parser.immersive_parser import ImmersiveDocParser
from utils.config import DOCUMENTATION_DIR, DATA_DIR
from utils.logger import logger


def parse_technical_documentation() -> dict:
    """
    Parse technical D&D documentation
    
    Returns:
        Dict with races and classes data
    """
    logger.info("Parsing technical documentation...")
    
    technical_dir = DOCUMENTATION_DIR
    extractor = RuleExtractor(technical_dir)
    
    try:
        rules = extractor.extract_all_rules()
        logger.info(f"✅ Extracted {len(rules['races'])} races")
        logger.info(f"✅ Extracted {len(rules['classes'])} classes")
        return rules
    except Exception as e:
        logger.error(f"Error parsing technical docs: {e}")
        return {'races': {}, 'classes': {}, 'version': '5e'}


def parse_immersive_documentation() -> dict:
    """
    Parse immersive first-person documentation
    
    Returns:
        Dict with immersive fragments
    """
    logger.info("Parsing immersive documentation...")
    
    immersive_dir = DOCUMENTATION_DIR / "Immersive"
    
    if not immersive_dir.exists():
        logger.warning(f"Immersive directory not found: {immersive_dir}")
        return {
            'races': [],
            'classes': [],
            'stats': [],
            'alignments': []
        }
    
    parser = ImmersiveDocParser(immersive_dir)
    
    try:
        fragments = parser.parse_all_immersive_docs()
        
        total = sum(len(v) for v in fragments.values())
        logger.info(f"✅ Extracted {total} immersive fragments")
        logger.info(f"   - Races: {len(fragments['races'])}")
        logger.info(f"   - Classes: {len(fragments['classes'])}")
        logger.info(f"   - Stats: {len(fragments['stats'])}")
        logger.info(f"   - Alignments: {len(fragments['alignments'])}")
        
        return fragments
    except Exception as e:
        logger.error(f"Error parsing immersive docs: {e}")
        return {
            'races': [],
            'classes': [],
            'stats': [],
            'alignments': []
        }


def generate_alignments_data() -> dict:
    """
    Generate alignment descriptions
    
    Returns:
        Dict with alignment data
    """
    return {
        "Lawful Good": {
            "short": "LG",
            "description": "Acts with compassion and honor within rules",
            "keywords": ["honor", "justice", "order", "compassion"]
        },
        "Neutral Good": {
            "short": "NG",
            "description": "Does good without bias toward or against order",
            "keywords": ["kindness", "altruism", "balance", "compassion"]
        },
        "Chaotic Good": {
            "short": "CG",
            "description": "Acts according to conscience, with little regard for rules",
            "keywords": ["freedom", "kindness", "independence", "rebellion"]
        },
        "Lawful Neutral": {
            "short": "LN",
            "description": "Acts in accordance with law, tradition, or personal codes",
            "keywords": ["order", "tradition", "reliability", "discipline"]
        },
        "True Neutral": {
            "short": "N",
            "description": "Avoids moral and ethical biases",
            "keywords": ["balance", "nature", "pragmatism", "neutrality"]
        },
        "Chaotic Neutral": {
            "short": "CN",
            "description": "Follows whims, values personal freedom above all",
            "keywords": ["freedom", "independence", "unpredictability", "self-interest"]
        },
        "Lawful Evil": {
            "short": "LE",
            "description": "Takes what they want within limits of tradition and order",
            "keywords": ["tyranny", "domination", "order", "cruelty"]
        },
        "Neutral Evil": {
            "short": "NE",
            "description": "Does whatever they can get away with, without compassion",
            "keywords": ["selfishness", "cruelty", "pragmatism", "malice"]
        },
        "Chaotic Evil": {
            "short": "CE",
            "description": "Acts with arbitrary violence, driven by greed and hatred",
            "keywords": ["destruction", "chaos", "cruelty", "violence"]
        }
    }


def generate_ability_scores_data() -> dict:
    """
    Generate ability scores reference data
    
    Returns:
        Dict with ability score information
    """
    return {
        "Strength": {
            "short": "STR",
            "description": "Physical power",
            "uses": ["melee attacks", "athletics", "carrying capacity"]
        },
        "Dexterity": {
            "short": "DEX",
            "description": "Agility and reflexes",
            "uses": ["AC", "initiative", "ranged attacks", "stealth"]
        },
        "Constitution": {
            "short": "CON",
            "description": "Endurance and health",
            "uses": ["hit points", "concentration", "poison resistance"]
        },
        "Intelligence": {
            "short": "INT",
            "description": "Reasoning and memory",
            "uses": ["investigation", "arcana", "history", "nature"]
        },
        "Wisdom": {
            "short": "WIS",
            "description": "Awareness and insight",
            "uses": ["perception", "insight", "medicine", "survival"]
        },
        "Charisma": {
            "short": "CHA",
            "description": "Force of personality",
            "uses": ["persuasion", "deception", "intimidation", "performance"]
        }
    }


def build_complete_database() -> dict:
    """
    Build complete rules database
    
    Returns:
        Comprehensive rules database
    """
    logger.info("="*70)
    logger.info("BUILDING COMPLETE RULES DATABASE")
    logger.info("="*70)
    
    # Parse technical docs
    technical_data = parse_technical_documentation()
    
    # Parse immersive docs
    immersive_data = parse_immersive_documentation()
    
    # Generate reference data
    alignments = generate_alignments_data()
    abilities = generate_ability_scores_data()
    
    # Build database
    database = {
        "metadata": {
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "dnd_version": "5e",
            "description": "WhytDD D&D 5e Rules Database"
        },
        "technical": {
            "races": technical_data.get('races', {}),
            "classes": technical_data.get('classes', {}),
            "alignments": alignments,
            "abilities": abilities
        },
        "immersive": {
            "races_fragments": immersive_data.get('races', []),
            "classes_fragments": immersive_data.get('classes', []),
            "stats_fragments": immersive_data.get('stats', []),
            "alignments_fragments": immersive_data.get('alignments', [])
        },
        "statistics": {
            "total_races": len(technical_data.get('races', {})),
            "total_classes": len(technical_data.get('classes', {})),
            "total_immersive_fragments": sum(
                len(v) for v in immersive_data.values()
            ),
            "total_alignments": len(alignments),
            "total_abilities": len(abilities)
        }
    }
    
    return database


def save_database(database: dict, filepath: Path):
    """
    Save database to JSON file
    
    Args:
        database: Database dictionary
        filepath: Output file path
    """
    logger.info(f"Saving database to {filepath}")
    
    # Ensure directory exists
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Save with pretty formatting
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2, ensure_ascii=False)
    
    # Get file size
    size_kb = filepath.stat().st_size / 1024
    logger.info(f"✅ Database saved ({size_kb:.2f} KB)")


def validate_database(database: dict) -> bool:
    """
    Validate database structure
    
    Args:
        database: Database to validate
        
    Returns:
        True if valid
    """
    logger.info("Validating database structure...")
    
    required_keys = ['metadata', 'technical', 'immersive', 'statistics']
    
    for key in required_keys:
        if key not in database:
            logger.error(f"❌ Missing required key: {key}")
            return False
    
    # Check metadata
    if 'version' not in database['metadata']:
        logger.error("❌ Missing version in metadata")
        return False
    
    # Check technical data
    if 'races' not in database['technical']:
        logger.error("❌ Missing races in technical data")
        return False
    
    # Check immersive data
    if 'races_fragments' not in database['immersive']:
        logger.error("❌ Missing races_fragments in immersive data")
        return False
    
    logger.info("✅ Database structure valid")
    return True


def main():
    """Main execution"""
    print("\n" + "="*70)
    print("WHYTDD - RULES DATABASE GENERATION")
    print("="*70 + "\n")
    
    # Build database
    database = build_complete_database()
    
    # Validate
    if not validate_database(database):
        logger.error("❌ Database validation failed")
        sys.exit(1)
    
    # Save
    output_path = DATA_DIR / "rules_database.json"
    save_database(database, output_path)
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"📊 Statistics:")
    for key, value in database['statistics'].items():
        print(f"   {key}: {value}")
    print(f"\n💾 Output: {output_path}")
    print(f"📏 Size: {output_path.stat().st_size / 1024:.2f} KB")
    print("\n✅ Rules database generated successfully!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
