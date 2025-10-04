"""
Tests for Complete Character Creation
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from character_creator.creator_logic import CharacterGenerator
from character_creator.equipment_manager import EquipmentBuilder
from knowledge_parser.data_validator import CharacterPersonality


def test_create_dwarf_fighter():
    """Test: Create Bruenor Battlehammer (Mountain Dwarf Fighter)"""
    print("\n" + "="*70)
    print("TEST: Create Mountain Dwarf Fighter")
    print("="*70)
    
    generator = CharacterGenerator()
    
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
        bonds=["I would die to recover an ancient relic of my clan"],
        flaws=["I have a weakness for the vices of the city"]
    )
    
    try:
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
        
        print(f"   ✅ Character created successfully")
        print(f"\n   Details:")
        print(f"      Name: {character.identity.name}")
        print(f"      Race: {character.identity.race} ({character.identity.subrace})")
        print(f"      Class: {character.identity.class_name} (Level {character.identity.level})")
        print(f"      Alignment: {character.identity.alignment}")
        
        # Check racial bonuses applied
        expected_str = 17  # 15 + 2 (Mountain Dwarf)
        expected_con = 17  # 15 + 2 (Dwarf)
        
        str_correct = character.stats.abilities.strength == expected_str
        con_correct = character.stats.abilities.constitution == expected_con
        
        print(f"\n   Stats (with racial bonuses):")
        print(f"      STR: {character.stats.abilities.strength} {'✅' if str_correct else '❌'} (expected {expected_str})")
        print(f"      CON: {character.stats.abilities.constitution} {'✅' if con_correct else '❌'} (expected {expected_con})")
        
        # Check HP
        con_mod = (character.stats.abilities.constitution - 10) // 2
        expected_hp = 10 + con_mod  # Fighter d10 + CON mod
        hp_correct = character.stats.hp_max == expected_hp
        
        print(f"\n   Combat Stats:")
        print(f"      HP: {character.stats.hp_max} {'✅' if hp_correct else '❌'} (expected {expected_hp})")
        print(f"      AC: {character.stats.ac}")
        print(f"      Proficiency: +{character.stats.proficiency_bonus}")
        
        # Check features
        has_features = len(character.features) > 0
        print(f"\n   Features: {len(character.features)} {'✅' if has_features else '❌'}")
        if has_features:
            for feature in character.features[:3]:
                print(f"      - {feature}")
        
        # Check equipment
        has_equipment = len(character.equipment) > 0
        print(f"\n   Equipment: {len(character.equipment)} {'✅' if has_equipment else '❌'}")
        if has_equipment:
            for item in character.equipment[:3]:
                print(f"      - {item}")
        
        # Validate all checks
        all_valid = str_correct and con_correct and hp_correct and has_features and has_equipment
        
        if all_valid:
            print(f"\n   ✅ All validations passed")
        else:
            print(f"\n   ❌ Some validations failed")
        
        return all_valid
        
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False


def test_create_elf_wizard():
    """Test: Create High Elf Wizard"""
    print("\n" + "="*70)
    print("TEST: Create High Elf Wizard")
    print("="*70)
    
    generator = CharacterGenerator()
    
    abilities = {
        'Strength': 8,
        'Dexterity': 14,
        'Constitution': 12,
        'Intelligence': 15,
        'Wisdom': 10,
        'Charisma': 13
    }
    
    try:
        character = generator.create_character(
            name="Taako",
            race="Elf",
            subrace="High Elf",
            class_name="Wizard",
            alignment="Chaotic Good",
            abilities=abilities,
            background="Sage"
        )
        
        print(f"   ✅ Character created successfully")
        print(f"\n   Details:")
        print(f"      Name: {character.identity.name}")
        print(f"      Race: {character.identity.race} ({character.identity.subrace})")
        print(f"      Class: {character.identity.class_name}")
        
        # Check racial bonuses applied
        expected_dex = 16  # 14 + 2 (Elf)
        expected_int = 16  # 15 + 1 (High Elf)
        
        dex_correct = character.stats.abilities.dexterity == expected_dex
        int_correct = character.stats.abilities.intelligence == expected_int
        
        print(f"\n   Stats (with racial bonuses):")
        print(f"      DEX: {character.stats.abilities.dexterity} {'✅' if dex_correct else '❌'} (expected {expected_dex})")
        print(f"      INT: {character.stats.abilities.intelligence} {'✅' if int_correct else '❌'} (expected {expected_int})")
        
        # Check HP (Wizard d6)
        con_mod = (character.stats.abilities.constitution - 10) // 2
        expected_hp = 6 + con_mod
        hp_correct = character.stats.hp_max == expected_hp
        
        print(f"\n   Combat Stats:")
        print(f"      HP: {character.stats.hp_max} {'✅' if hp_correct else '❌'} (expected {expected_hp})")
        print(f"      AC: {character.stats.ac}")
        
        all_valid = dex_correct and int_correct and hp_correct
        
        if all_valid:
            print(f"\n   ✅ All validations passed")
        else:
            print(f"\n   ❌ Some validations failed")
        
        return all_valid
        
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False


def test_create_human_rogue():
    """Test: Create Human Rogue"""
    print("\n" + "="*70)
    print("TEST: Create Human Rogue")
    print("="*70)
    
    generator = CharacterGenerator()
    
    abilities = {
        'Strength': 10,
        'Dexterity': 15,
        'Constitution': 12,
        'Intelligence': 13,
        'Wisdom': 11,
        'Charisma': 14
    }
    
    try:
        character = generator.create_character(
            name="Vax'ildan",
            race="Human",
            class_name="Rogue",
            alignment="Chaotic Good",
            abilities=abilities,
            background="Criminal"
        )
        
        print(f"   ✅ Character created successfully")
        
        # Check racial bonuses (Human +1 all)
        all_increased = all(
            getattr(character.stats.abilities, ability.lower()) == abilities[ability] + 1
            for ability in abilities.keys()
        )
        
        print(f"   Stats bonus (Human +1 all): {'✅' if all_increased else '❌'}")
        
        # Check HP (Rogue d8)
        con_mod = (character.stats.abilities.constitution - 10) // 2
        expected_hp = 8 + con_mod
        hp_correct = character.stats.hp_max == expected_hp
        
        print(f"   HP: {character.stats.hp_max} {'✅' if hp_correct else '❌'} (expected {expected_hp})")
        
        all_valid = all_increased and hp_correct
        
        if all_valid:
            print(f"\n   ✅ All validations passed")
        else:
            print(f"\n   ❌ Some validations failed")
        
        return all_valid
        
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False


def test_equipment_ac_calculation():
    """Test: Equipment AC Calculation"""
    print("\n" + "="*70)
    print("TEST: AC Calculation")
    print("="*70)
    
    builder = EquipmentBuilder()
    
    test_cases = [
        # (dex, armor, shield, expected_ac, description)
        (14, None, False, 12, "Unarmored (DEX 14)"),
        (16, 'Leather', False, 14, "Leather armor (DEX 16)"),
        (16, 'Leather', True, 16, "Leather + Shield (DEX 16)"),
        (12, 'Chain Mail', True, 18, "Chain Mail + Shield (DEX 12)"),
        (18, 'Studded Leather', False, 16, "Studded Leather (DEX 18)"),
    ]
    
    passed = 0
    failed = 0
    
    for dex, armor, shield, expected, desc in test_cases:
        ac, explanation = builder.calculate_ac(dex, armor, shield)
        
        if ac == expected:
            print(f"   ✅ {desc}: AC {ac}")
            passed += 1
        else:
            print(f"   ❌ {desc}: AC {ac} (expected {expected})")
            print(f"      Calculation: {explanation}")
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_behavioral_profile_integration():
    """Test: Behavioral Profile Integration"""
    print("\n" + "="*70)
    print("TEST: Behavioral Profile Integration")
    print("="*70)
    
    generator = CharacterGenerator()
    
    abilities = {
        'Strength': 17,
        'Dexterity': 10,
        'Constitution': 16,
        'Intelligence': 8,
        'Wisdom': 12,
        'Charisma': 10
    }
    
    try:
        character = generator.create_character(
            name="Grog Strongjaw",
            race="Half-Orc",
            class_name="Barbarian",
            alignment="Chaotic Neutral",
            abilities=abilities
        )
        
        # Check if behavioral profile was generated
        char_dict = character.dict()
        has_profile = 'behavioral_profile' in char_dict
        
        if has_profile:
            profile = char_dict['behavioral_profile']
            directive_count = profile.get('total_directives', 0)
            has_reasonable_count = 20 <= directive_count <= 50
            
            print(f"   ✅ Behavioral profile generated")
            print(f"   Total directives: {directive_count} {'✅' if has_reasonable_count else '❌'}")
            
            # Show categories
            print(f"\n   Breakdown:")
            print(f"      Stats: {len(profile.get('stat_behaviors', []))}")
            print(f"      Race: {len(profile.get('racial_behaviors', []))}")
            print(f"      Class: {len(profile.get('class_behaviors', []))}")
            print(f"      Alignment: {len(profile.get('alignment_behaviors', []))}")
            
            # Show sample
            print(f"\n   Sample directives:")
            for i, directive in enumerate(profile['all_directives'][:3], 1):
                print(f"      {i}. {directive}")
            
            return has_profile and has_reasonable_count
        else:
            print(f"   ❌ No behavioral profile found")
            return False
        
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False


def run_all_tests():
    """Run all character creation tests"""
    print("\n" + "="*70)
    print("CHARACTER CREATION - TEST SUITE")
    print("="*70)
    
    tests = [
        ("Create Dwarf Fighter", test_create_dwarf_fighter),
        ("Create Elf Wizard", test_create_elf_wizard),
        ("Create Human Rogue", test_create_human_rogue),
        ("AC Calculation", test_equipment_ac_calculation),
        ("Behavioral Profile Integration", test_behavioral_profile_integration)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n   ❌ EXCEPTION: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    failed = len(results) - passed
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status}: {test_name}")
    
    print(f"\n   Total: {passed}/{len(results)} tests passed")
    
    if failed == 0:
        print("\n   🎉 ALL TESTS PASSED!")
    else:
        print(f"\n   ⚠️  {failed} test(s) failed")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
