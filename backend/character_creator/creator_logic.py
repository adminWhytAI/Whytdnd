"""
Creator Logic - Main character creation orchestration
Combines all components to create complete D&D 5e characters
"""
from typing import Dict, List, Optional
from datetime import datetime
import uuid

from backend.character_creator.stats_calculator import StatsManager
from backend.character_creator.behavioral_translator import BehavioralProfileBuilder
from backend.knowledge_parser.data_validator import (
    CharacterCreate,
    CharacterComplete,
    CharacterStats,
    CharacterIdentity,
    CharacterPersonality,
    AbilityScores
)
from backend.utils.logger import logger
from backend.utils.exceptions import InvalidCharacterDataError


class CharacterGenerator:
    """
    Main character generation orchestrator
    """
    
    def __init__(self, rules_database: Optional[Dict] = None):
        """
        Args:
            rules_database: Optional pre-loaded rules database
        """
        self.rules_database = rules_database
        self.stats_manager = StatsManager()
        self.behavioral_builder = BehavioralProfileBuilder()
    
    def create_character(
        self,
        name: str,
        race: str,
        class_name: str,
        alignment: str,
        abilities: Dict[str, int],
        subrace: Optional[str] = None,
        background: Optional[str] = None,
        personality: Optional[CharacterPersonality] = None
    ) -> CharacterComplete:
        """
        Create a complete character
        
        Args:
            name: Character name
            race: Character race
            class_name: Character class
            alignment: Character alignment
            abilities: Base ability scores (before racial bonuses)
            subrace: Optional subrace
            background: Optional background
            personality: Optional personality traits
            
        Returns:
            Complete character data
        """
        logger.info(f"Creating character: {name} ({race} {class_name})")
        
        # Generate unique ID
        char_id = self._generate_character_id()
        
        # Apply racial bonuses
        racial_bonuses = self._get_racial_bonuses(race, subrace)
        final_abilities = self.stats_manager.apply_racial_bonuses(
            abilities,
            racial_bonuses
        )
        
        # Calculate derived stats
        hp_max = self._calculate_starting_hp(class_name, final_abilities['Constitution'])
        ac = self._calculate_base_ac(final_abilities['Dexterity'])
        proficiency_bonus = 2  # Always 2 at level 1
        
        # Get class features
        features = self._get_starting_features(race, class_name, subrace)
        
        # Get starting equipment
        equipment = self._get_starting_equipment(class_name, background)
        
        # Build behavioral profile
        behavioral_profile = self.behavioral_builder.build_complete_profile(
            abilities=final_abilities,
            race=race,
            class_name=class_name,
            alignment=alignment,
            subrace=subrace,
            personality_traits=personality.personality_traits if personality else None
        )
        
        # Create character object
        identity = CharacterIdentity(
            name=name,
            race=race,
            subrace=subrace,
            class_name=class_name,
            level=1,
            alignment=alignment,
            background=background
        )
        
        stats = CharacterStats(
            abilities=AbilityScores(**final_abilities),
            hp_max=hp_max,
            hp_current=hp_max,
            ac=ac,
            proficiency_bonus=proficiency_bonus
        )
        
        character = CharacterComplete(
            id=char_id,
            identity=identity,
            stats=stats,
            personality=personality or CharacterPersonality(),
            features=features,
            equipment=equipment,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        # Attach behavioral profile (not in Pydantic schema, added dynamically)
        character_dict = character.dict()
        character_dict['behavioral_profile'] = behavioral_profile
        
        logger.info(f"✅ Character created: {name} (ID: {char_id})")
        
        return character
    
    def _generate_character_id(self) -> str:
        """Generate unique character ID"""
        return str(uuid.uuid4())[:8]
    
    def _get_racial_bonuses(self, race: str, subrace: Optional[str]) -> Dict[str, int]:
        """
        Get racial ability score bonuses
        
        Args:
            race: Character race
            subrace: Optional subrace
            
        Returns:
            Dict of ability bonuses
        """
        # Simplified - in production, load from rules_database
        bonuses = {}
        race_lower = race.lower()
        
        if 'dwarf' in race_lower:
            bonuses['Constitution'] = 2
            if subrace and 'mountain' in subrace.lower():
                bonuses['Strength'] = 2
            elif subrace and 'hill' in subrace.lower():
                bonuses['Wisdom'] = 1
                
        elif 'elf' in race_lower:
            bonuses['Dexterity'] = 2
            if subrace and 'high' in subrace.lower():
                bonuses['Intelligence'] = 1
            elif subrace and 'wood' in subrace.lower():
                bonuses['Wisdom'] = 1
                
        elif 'human' in race_lower:
            # +1 to all
            for ability in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
                bonuses[ability] = 1
                
        elif 'halfling' in race_lower:
            bonuses['Dexterity'] = 2
            if subrace and 'lightfoot' in subrace.lower():
                bonuses['Charisma'] = 1
            elif subrace and 'stout' in subrace.lower():
                bonuses['Constitution'] = 1
                
        elif 'dragonborn' in race_lower:
            bonuses['Strength'] = 2
            bonuses['Charisma'] = 1
            
        elif 'half-orc' in race_lower or 'half orc' in race_lower:
            bonuses['Strength'] = 2
            bonuses['Constitution'] = 1
            
        elif 'tiefling' in race_lower:
            bonuses['Charisma'] = 2
            bonuses['Intelligence'] = 1
        
        logger.debug(f"Racial bonuses for {race} {subrace}: {bonuses}")
        return bonuses
    
    def _calculate_starting_hp(self, class_name: str, constitution: int) -> int:
        """
        Calculate starting HP at level 1
        
        Args:
            class_name: Character class
            constitution: Constitution score
            
        Returns:
            Max HP
        """
        # Get hit die for class
        hit_dice = {
            'Fighter': 10,
            'Wizard': 6,
            'Rogue': 8,
            'Cleric': 8,
            'Paladin': 10,
            'Ranger': 10,
            'Barbarian': 12,
            'Bard': 8,
            'Druid': 8,
            'Monk': 8,
            'Sorcerer': 6,
            'Warlock': 8
        }
        
        hit_die = hit_dice.get(class_name, 8)
        con_modifier = self.stats_manager.calculate_modifier(constitution)
        
        # Level 1: max hit die + CON modifier
        hp = hit_die + con_modifier
        
        logger.debug(f"Starting HP: {hit_die} (hit die) + {con_modifier} (CON) = {hp}")
        return max(1, hp)  # Minimum 1 HP
    
    def _calculate_base_ac(self, dexterity: int) -> int:
        """
        Calculate base AC (10 + DEX modifier)
        
        Args:
            dexterity: Dexterity score
            
        Returns:
            Base AC
        """
        dex_modifier = self.stats_manager.calculate_modifier(dexterity)
        return 10 + dex_modifier
    
    def _get_starting_features(
        self,
        race: str,
        class_name: str,
        subrace: Optional[str]
    ) -> List[str]:
        """
        Get starting racial and class features
        
        Args:
            race: Character race
            class_name: Character class
            subrace: Optional subrace
            
        Returns:
            List of feature names
        """
        features = []
        
        # Racial features (simplified)
        race_lower = race.lower()
        
        if 'dwarf' in race_lower:
            features.extend(['Darkvision', 'Dwarven Resilience', 'Stonecunning'])
            if subrace and 'mountain' in subrace.lower():
                features.append('Dwarven Armor Training')
                
        elif 'elf' in race_lower:
            features.extend(['Darkvision', 'Fey Ancestry', 'Trance'])
            if subrace and 'high' in subrace.lower():
                features.append('Cantrip')
                
        elif 'human' in race_lower:
            features.append('Versatile')
            
        elif 'halfling' in race_lower:
            features.extend(['Lucky', 'Brave', 'Halfling Nimbleness'])
        
        # Class features (simplified - level 1 only)
        class_features = {
            'Fighter': ['Fighting Style', 'Second Wind'],
            'Wizard': ['Spellcasting', 'Arcane Recovery'],
            'Rogue': ['Expertise', 'Sneak Attack', 'Thieves Cant'],
            'Cleric': ['Spellcasting', 'Divine Domain'],
            'Paladin': ['Divine Sense', 'Lay on Hands'],
            'Barbarian': ['Rage', 'Unarmored Defense'],
            'Bard': ['Spellcasting', 'Bardic Inspiration'],
            'Ranger': ['Favored Enemy', 'Natural Explorer'],
            'Monk': ['Unarmored Defense', 'Martial Arts'],
            'Druid': ['Druidic', 'Spellcasting'],
            'Sorcerer': ['Spellcasting', 'Sorcerous Origin'],
            'Warlock': ['Otherworldly Patron', 'Pact Magic']
        }
        
        features.extend(class_features.get(class_name, []))
        
        return features
    
    def _get_starting_equipment(
        self,
        class_name: str,
        background: Optional[str]
    ) -> List[str]:
        """
        Get starting equipment for class
        
        Args:
            class_name: Character class
            background: Optional background
            
        Returns:
            List of equipment items
        """
        # Simplified starting equipment
        equipment_by_class = {
            'Fighter': [
                'Chain mail',
                'Longsword',
                'Shield',
                'Light crossbow',
                '20 bolts',
                'Explorers pack'
            ],
            'Wizard': [
                'Quarterstaff',
                'Component pouch',
                'Scholars pack',
                'Spellbook'
            ],
            'Rogue': [
                'Rapier',
                'Shortbow',
                '20 arrows',
                'Thieves tools',
                'Leather armor',
                'Burglars pack'
            ],
            'Cleric': [
                'Mace',
                'Scale mail',
                'Shield',
                'Holy symbol',
                'Priests pack'
            ]
        }
        
        equipment = equipment_by_class.get(class_name, ['Basic equipment'])
        
        # Add background equipment (simplified)
        if background:
            equipment.append(f'{background} equipment')
        
        return equipment


if __name__ == "__main__":
    # Test character creation
    print("="*70)
    print("TESTING CHARACTER CREATOR")
    print("="*70)
    
    generator = CharacterGenerator()
    
    # Create Bruenor Battlehammer
    print("\n📋 Creating: Bruenor Battlehammer")
    print("   Mountain Dwarf Fighter (Lawful Good)")
    
    abilities = {
        'Strength': 15,
        'Dexterity': 12,
        'Constitution': 15,
        'Intelligence': 10,
        'Wisdom': 13,
        'Charisma': 8
    }
    
    personality = CharacterPersonality(
        personality_traits=["I'm always polite and respectful"],
        ideals=["Honor"],
        bonds=["I would die to recover an ancient relic"],
        flaws=["I have a weakness for the vices of the city"]
    )
    
    character = generator.create_character(
        name="Bruenor Battlehammer",
        race="Dwarf",
        subrace="Mountain Dwarf",
        class_name="Fighter",
        alignment="Lawful Good",
        abilities=abilities,
        background="Soldier",
        personality=personality
    )
    
    print(f"\n✅ Character Created!")
    print(f"   ID: {character.id}")
    print(f"   Name: {character.identity.name}")
    print(f"   Race: {character.identity.race} ({character.identity.subrace})")
    print(f"   Class: {character.identity.class_name} (Level {character.identity.level})")
    print(f"   Alignment: {character.identity.alignment}")
    
    print(f"\n📊 Stats:")
    print(f"   STR: {character.stats.abilities.strength} ({character.stats.abilities.get_modifier('strength'):+d})")
    print(f"   DEX: {character.stats.abilities.dexterity} ({character.stats.abilities.get_modifier('dexterity'):+d})")
    print(f"   CON: {character.stats.abilities.constitution} ({character.stats.abilities.get_modifier('constitution'):+d})")
    print(f"   INT: {character.stats.abilities.intelligence} ({character.stats.abilities.get_modifier('intelligence'):+d})")
    print(f"   WIS: {character.stats.abilities.wisdom} ({character.stats.abilities.get_modifier('wisdom'):+d})")
    print(f"   CHA: {character.stats.abilities.charisma} ({character.stats.abilities.get_modifier('charisma'):+d})")
    
    print(f"\n⚔️  Combat Stats:")
    print(f"   HP: {character.stats.hp_current}/{character.stats.hp_max}")
    print(f"   AC: {character.stats.ac}")
    print(f"   Proficiency: +{character.stats.proficiency_bonus}")
    
    print(f"\n🎭 Features ({len(character.features)}):")
    for feature in character.features[:5]:
        print(f"   - {feature}")
    
    print(f"\n🎒 Equipment ({len(character.equipment)}):")
    for item in character.equipment[:5]:
        print(f"   - {item}")
    
    # Access behavioral profile (added dynamically)
    char_dict = character.dict()
    if 'behavioral_profile' in char_dict:
        profile = char_dict['behavioral_profile']
        print(f"\n🎭 Behavioral Profile:")
        print(f"   Total Directives: {profile['total_directives']}")
        print(f"\n   Sample Directives:")
        for i, directive in enumerate(profile['all_directives'][:5], 1):
            print(f"   {i}. {directive}")
    
    print("\n✅ Character creation complete!")
