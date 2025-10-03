"""
Equipment Manager - Handles starting equipment and AC calculation
"""
from typing import Dict, List, Optional, Tuple
from backend.utils.logger import logger


class EquipmentBuilder:
    """
    Manages character equipment and armor class calculations
    """
    
    # Armor AC values
    ARMOR_AC = {
        # Light Armor (AC + DEX)
        'Padded': 11,
        'Leather': 11,
        'Studded Leather': 12,
        
        # Medium Armor (AC + DEX, max +2)
        'Hide': 12,
        'Chain Shirt': 13,
        'Scale Mail': 14,
        'Breastplate': 14,
        'Half Plate': 15,
        
        # Heavy Armor (AC only, no DEX)
        'Ring Mail': 14,
        'Chain Mail': 16,
        'Splint': 17,
        'Plate': 18
    }
    
    # Shield bonus
    SHIELD_AC_BONUS = 2
    
    def __init__(self):
        """Initialize equipment builder"""
        pass
    
    def get_starting_equipment(
        self,
        class_name: str,
        background: Optional[str] = None
    ) -> List[str]:
        """
        Get starting equipment based on class and background
        
        Args:
            class_name: Character class
            background: Optional background
            
        Returns:
            List of equipment items
        """
        logger.debug(f"Getting starting equipment for {class_name}")
        
        equipment = []
        
        # Class equipment (PHB starting equipment)
        class_equipment = {
            'Barbarian': [
                'Greataxe',
                '2 handaxes',
                '4 javelins',
                'Explorers pack'
            ],
            'Bard': [
                'Rapier',
                'Lute',
                'Leather armor',
                'Dagger',
                'Entertainers pack'
            ],
            'Cleric': [
                'Mace',
                'Scale mail',
                'Shield',
                'Holy symbol',
                'Priests pack'
            ],
            'Druid': [
                'Wooden shield',
                'Scimitar',
                'Leather armor',
                'Explorers pack',
                'Druidic focus'
            ],
            'Fighter': [
                'Chain mail',
                'Longsword',
                'Shield',
                'Light crossbow',
                '20 bolts',
                'Explorers pack'
            ],
            'Monk': [
                '10 darts',
                'Shortsword',
                'Dungeoneer\'s pack'
            ],
            'Paladin': [
                'Chain mail',
                'Longsword',
                'Shield',
                '5 javelins',
                'Priests pack',
                'Holy symbol'
            ],
            'Ranger': [
                'Scale mail',
                'Longsword',
                '2 shortswords',
                'Longbow',
                '20 arrows',
                'Explorers pack'
            ],
            'Rogue': [
                'Rapier',
                'Shortbow',
                '20 arrows',
                'Leather armor',
                'Thieves tools',
                '2 daggers',
                'Burglars pack'
            ],
            'Sorcerer': [
                'Light crossbow',
                '20 bolts',
                'Component pouch',
                'Dungeoneer\'s pack',
                '2 daggers'
            ],
            'Warlock': [
                'Light crossbow',
                '20 bolts',
                'Leather armor',
                'Component pouch',
                'Scholars pack',
                '2 daggers'
            ],
            'Wizard': [
                'Quarterstaff',
                'Component pouch',
                'Scholars pack',
                'Spellbook'
            ]
        }
        
        equipment.extend(class_equipment.get(class_name, ['Basic equipment']))
        
        # Background equipment (simplified)
        background_equipment = {
            'Acolyte': ['Holy symbol', 'Prayer book', 'Incense', 'Vestments', 'Common clothes', '15 gp'],
            'Criminal': ['Crowbar', 'Dark clothes with hood', 'Belt pouch', '15 gp'],
            'Folk Hero': ['Artisan tools', 'Shovel', 'Iron pot', 'Common clothes', 'Belt pouch', '10 gp'],
            'Noble': ['Fine clothes', 'Signet ring', 'Scroll of pedigree', 'Purse', '25 gp'],
            'Sage': ['Ink', 'Quill', 'Small knife', 'Letter', 'Common clothes', '10 gp'],
            'Soldier': ['Insignia of rank', 'Trophy', 'Dice set', 'Common clothes', '10 gp']
        }
        
        if background and background in background_equipment:
            equipment.extend(background_equipment[background])
        
        logger.debug(f"Starting equipment: {len(equipment)} items")
        return equipment
    
    def calculate_ac(
        self,
        dexterity: int,
        armor: Optional[str] = None,
        has_shield: bool = False,
        unarmored_defense: Optional[str] = None,
        wisdom: Optional[int] = None,
        constitution: Optional[int] = None
    ) -> Tuple[int, str]:
        """
        Calculate armor class
        
        Args:
            dexterity: DEX score
            armor: Armor worn (None for unarmored)
            has_shield: Whether character has a shield
            unarmored_defense: Type of unarmored defense (Barbarian/Monk)
            wisdom: WIS score (for Monk)
            constitution: CON score (for Barbarian)
            
        Returns:
            (AC value, AC calculation explanation)
        """
        dex_modifier = (dexterity - 10) // 2
        ac = 10
        explanation = "10 (base)"
        
        # Unarmored Defense (Barbarian or Monk)
        if unarmored_defense and not armor:
            if unarmored_defense == 'Barbarian' and constitution:
                con_modifier = (constitution - 10) // 2
                ac = 10 + dex_modifier + con_modifier
                explanation = f"10 + {dex_modifier} (DEX) + {con_modifier} (CON)"
            elif unarmored_defense == 'Monk' and wisdom:
                wis_modifier = (wisdom - 10) // 2
                ac = 10 + dex_modifier + wis_modifier
                explanation = f"10 + {dex_modifier} (DEX) + {wis_modifier} (WIS)"
        
        # Armored
        elif armor:
            base_ac = self.ARMOR_AC.get(armor, 10)
            ac = base_ac
            explanation = f"{base_ac} ({armor})"
            
            # Light armor: full DEX bonus
            if armor in ['Padded', 'Leather', 'Studded Leather']:
                ac += dex_modifier
                explanation += f" + {dex_modifier} (DEX)"
            
            # Medium armor: DEX bonus (max +2)
            elif armor in ['Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate', 'Half Plate']:
                dex_bonus = min(dex_modifier, 2)
                ac += dex_bonus
                explanation += f" + {dex_bonus} (DEX, max +2)"
            
            # Heavy armor: no DEX bonus
            # (already included in base_ac)
        
        # No armor, no unarmored defense
        else:
            ac = 10 + dex_modifier
            explanation = f"10 + {dex_modifier} (DEX)"
        
        # Shield bonus
        if has_shield:
            ac += self.SHIELD_AC_BONUS
            explanation += f" + {self.SHIELD_AC_BONUS} (shield)"
        
        logger.debug(f"Calculated AC: {ac} ({explanation})")
        return ac, explanation
    
    def get_armor_proficiencies(self, class_name: str) -> List[str]:
        """
        Get armor proficiencies for a class
        
        Args:
            class_name: Character class
            
        Returns:
            List of armor proficiencies
        """
        proficiencies = {
            'Barbarian': ['Light armor', 'Medium armor', 'Shields'],
            'Bard': ['Light armor'],
            'Cleric': ['Light armor', 'Medium armor', 'Shields'],
            'Druid': ['Light armor', 'Medium armor', 'Shields (non-metal)'],
            'Fighter': ['All armor', 'Shields'],
            'Monk': [],  # Unarmored Defense
            'Paladin': ['All armor', 'Shields'],
            'Ranger': ['Light armor', 'Medium armor', 'Shields'],
            'Rogue': ['Light armor'],
            'Sorcerer': [],
            'Warlock': ['Light armor'],
            'Wizard': []
        }
        
        return proficiencies.get(class_name, [])
    
    def get_weapon_proficiencies(self, class_name: str) -> List[str]:
        """
        Get weapon proficiencies for a class
        
        Args:
            class_name: Character class
            
        Returns:
            List of weapon proficiencies
        """
        proficiencies = {
            'Barbarian': ['Simple weapons', 'Martial weapons'],
            'Bard': ['Simple weapons', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
            'Cleric': ['Simple weapons'],
            'Druid': ['Clubs', 'Daggers', 'Darts', 'Javelins', 'Maces', 'Quarterstaffs', 'Scimitars', 'Sickles', 'Slings', 'Spears'],
            'Fighter': ['Simple weapons', 'Martial weapons'],
            'Monk': ['Simple weapons', 'Shortswords'],
            'Paladin': ['Simple weapons', 'Martial weapons'],
            'Ranger': ['Simple weapons', 'Martial weapons'],
            'Rogue': ['Simple weapons', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
            'Sorcerer': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows'],
            'Warlock': ['Simple weapons'],
            'Wizard': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows']
        }
        
        return proficiencies.get(class_name, [])
    
    def can_wear_armor(self, class_name: str, armor: str) -> bool:
        """
        Check if a class can wear specific armor
        
        Args:
            class_name: Character class
            armor: Armor type
            
        Returns:
            True if proficient
        """
        proficiencies = self.get_armor_proficiencies(class_name)
        
        if 'All armor' in proficiencies:
            return True
        
        # Check armor category
        light_armor = ['Padded', 'Leather', 'Studded Leather']
        medium_armor = ['Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate', 'Half Plate']
        
        if armor in light_armor and 'Light armor' in proficiencies:
            return True
        
        if armor in medium_armor and 'Medium armor' in proficiencies:
            return True
        
        # Heavy armor requires explicit proficiency
        if 'Heavy armor' in proficiencies:
            return True
        
        return False


if __name__ == "__main__":
    # Test equipment manager
    print("="*70)
    print("TESTING EQUIPMENT MANAGER")
    print("="*70)
    
    builder = EquipmentBuilder()
    
    # Test starting equipment
    print("\n✅ Testing Starting Equipment:")
    for class_name in ['Fighter', 'Wizard', 'Rogue']:
        equipment = builder.get_starting_equipment(class_name, background='Soldier')
        print(f"\n{class_name}:")
        for item in equipment[:5]:
            print(f"   - {item}")
        if len(equipment) > 5:
            print(f"   ... and {len(equipment) - 5} more items")
    
    # Test AC calculation
    print("\n✅ Testing AC Calculation:")
    
    # Unarmored (DEX 14)
    ac, explanation = builder.calculate_ac(dexterity=14)
    print(f"\nUnarmored (DEX 14): AC {ac}")
    print(f"   {explanation}")
    
    # Leather armor + shield (DEX 16)
    ac, explanation = builder.calculate_ac(dexterity=16, armor='Leather', has_shield=True)
    print(f"\nLeather + Shield (DEX 16): AC {ac}")
    print(f"   {explanation}")
    
    # Chain mail + shield (DEX 12)
    ac, explanation = builder.calculate_ac(dexterity=12, armor='Chain Mail', has_shield=True)
    print(f"\nChain Mail + Shield (DEX 12): AC {ac}")
    print(f"   {explanation}")
    
    # Monk Unarmored Defense (DEX 16, WIS 14)
    ac, explanation = builder.calculate_ac(
        dexterity=16,
        wisdom=14,
        unarmored_defense='Monk'
    )
    print(f"\nMonk Unarmored Defense (DEX 16, WIS 14): AC {ac}")
    print(f"   {explanation}")
    
    # Barbarian Unarmored Defense (DEX 14, CON 16)
    ac, explanation = builder.calculate_ac(
        dexterity=14,
        constitution=16,
        unarmored_defense='Barbarian'
    )
    print(f"\nBarbarian Unarmored Defense (DEX 14, CON 16): AC {ac}")
    print(f"   {explanation}")
    
    # Test proficiencies
    print("\n✅ Testing Proficiencies:")
    print(f"\nFighter Armor: {builder.get_armor_proficiencies('Fighter')}")
    print(f"Wizard Armor: {builder.get_armor_proficiencies('Wizard')}")
    print(f"\nFighter can wear Chain Mail: {builder.can_wear_armor('Fighter', 'Chain Mail')}")
    print(f"Wizard can wear Chain Mail: {builder.can_wear_armor('Wizard', 'Chain Mail')}")
    
    print("\n✅ All tests complete!")
