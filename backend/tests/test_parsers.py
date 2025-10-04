"""
Tests for Knowledge Parser Modules
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from knowledge_parser.data_validator import (
    AbilityScores,
    CharacterCreate,
    RaceSchema,
    ClassSchema,
    validate_character_data
)


def test_ability_scores_validation():
    """Test: Ability Scores Validation"""
    print("\n" + "="*70)
    print("TEST: Ability Scores Validation")
    print("="*70)
    
    # Valid scores
    try:
        abilities = AbilityScores(
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=12,
            charisma=8
        )
        print(f"   ✅ Valid scores accepted")
        
        # Test modifier calculation
        str_mod = abilities.get_modifier('strength')
        expected = 3
        
        if str_mod == expected:
            print(f"   ✅ Modifier calculation correct: STR 16 → +{str_mod}")
        else:
            print(f"   ❌ Modifier calculation wrong: +{str_mod} (expected +{expected})")
            return False
        
    except Exception as e:
        print(f"   ❌ Valid scores rejected: {e}")
        return False
    
    # Invalid scores (out of range)
    try:
        abilities = AbilityScores(
            strength=35,  # Too high
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=12,
            charisma=8
        )
        print(f"   ❌ Invalid scores accepted (should reject)")
        return False
    except Exception:
        print(f"   ✅ Invalid scores rejected (35 > 30)")
    
    return True


def test_character_creation_validation():
    """Test: Character Creation Data Validation"""
    print("\n" + "="*70)
    print("TEST: Character Creation Validation")
    print("="*70)
    
    valid_data = {
        "identity": {
            "name": "Test Character",
            "race": "Human",
            "class": "Fighter",
            "level": 1,
            "alignment": "Neutral Good"
        },
        "abilities": {
            "strength": 16,
            "dexterity": 14,
            "constitution": 15,
            "intelligence": 10,
            "wisdom": 12,
            "charisma": 8
        }
    }
    
    try:
        character = validate_character_data(valid_data)
        print(f"   ✅ Valid character data accepted")
        print(f"      Name: {character.identity.name}")
        print(f"      Race: {character.identity.race}")
        print(f"      Class: {character.identity.class_name}")
        return True
    except Exception as e:
        print(f"   ❌ Valid character data rejected: {e}")
        return False


def test_race_schema_validation():
    """Test: Race Schema Validation"""
    print("\n" + "="*70)
    print("TEST: Race Schema Validation")
    print("="*70)
    
    valid_race = {
        "name": "Dwarf",
        "ability_score_increase": {"Constitution": 2},
        "size": "Medium",
        "speed": 25,
        "languages": ["Common", "Dwarvish"],
        "traits": [
            {
                "name": "Darkvision",
                "description": "See in dim light within 60 feet",
                "mechanical_effect": "60 ft darkvision"
            }
        ]
    }
    
    try:
        race = RaceSchema(**valid_race)
        print(f"   ✅ Valid race schema accepted")
        print(f"      Name: {race.name}")
        print(f"      Speed: {race.speed}")
        print(f"      Traits: {len(race.traits)}")
        return True
    except Exception as e:
        print(f"   ❌ Valid race schema rejected: {e}")
        return False


def test_class_schema_validation():
    """Test: Class Schema Validation"""
    print("\n" + "="*70)
    print("TEST: Class Schema Validation")
    print("="*70)
    
    valid_class = {
        "name": "Fighter",
        "hit_die": 10,
        "primary_ability": ["Strength", "Dexterity"],
        "saving_throws": ["Strength", "Constitution"],
        "armor_proficiencies": ["Light", "Medium", "Heavy", "Shields"],
        "weapon_proficiencies": ["Simple", "Martial"],
        "features": [
            {
                "name": "Fighting Style",
                "level": 1,
                "description": "Choose a fighting style"
            }
        ]
    }
    
    try:
        char_class = ClassSchema(**valid_class)
        print(f"   ✅ Valid class schema accepted")
        print(f"      Name: {char_class.name}")
        print(f"      Hit Die: d{char_class.hit_die}")
        print(f"      Features: {len(char_class.features)}")
        return True
    except Exception as e:
        print(f"   ❌ Valid class schema rejected: {e}")
        return False


def test_invalid_data_rejection():
    """Test: Invalid Data Rejection"""
    print("\n" + "="*70)
    print("TEST: Invalid Data Rejection")
    print("="*70)
    
    test_cases = [
        # Invalid ability scores
        {
            "identity": {
                "name": "Test",
                "race": "Human",
                "class": "Fighter",
                "level": 1,
                "alignment": "Good"
            },
            "abilities": {
                "strength": 100,  # Invalid
                "dexterity": 14,
                "constitution": 15,
                "intelligence": 10,
                "wisdom": 12,
                "charisma": 8
            }
        },
        # Missing required field
        {
            "identity": {
                "name": "Test",
                "race": "Human",
                # Missing class
                "level": 1,
                "alignment": "Good"
            },
            "abilities": {
                "strength": 16,
                "dexterity": 14,
                "constitution": 15,
                "intelligence": 10,
                "wisdom": 12,
                "charisma": 8
            }
        }
    ]
    
    passed = 0
    for i, invalid_data in enumerate(test_cases, 1):
        try:
            character = validate_character_data(invalid_data)
            print(f"   ❌ Test {i}: Invalid data accepted (should reject)")
        except Exception:
            print(f"   ✅ Test {i}: Invalid data correctly rejected")
            passed += 1
    
    return passed == len(test_cases)


def test_immersive_parser_structure():
    """Test: Immersive Parser Structure (without files)"""
    print("\n" + "="*70)
    print("TEST: Immersive Parser Structure")
    print("="*70)
    
    try:
        from knowledge_parser.immersive_parser import ImmersiveDocParser, FragmentExtractor
        
        # Check classes exist
        print(f"   ✅ ImmersiveDocParser class exists")
        print(f"   ✅ FragmentExtractor class exists")
        
        # Check methods exist
        parser = ImmersiveDocParser(Path("dummy"))
        has_methods = all(hasattr(parser, method) for method in [
            'parse_all_immersive_docs',
            'parse_file',
            '_split_into_sections',
            '_extract_first_person_content'
        ])
        
        if has_methods:
            print(f"   ✅ All required methods exist")
            return True
        else:
            print(f"   ❌ Some methods missing")
            return False
        
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False


def test_rule_parser_structure():
    """Test: Rule Parser Structure (without files)"""
    print("\n" + "="*70)
    print("TEST: Rule Parser Structure")
    print("="*70)
    
    try:
        from knowledge_parser.rule_parser import RaceParser, ClassParser, RuleExtractor
        
        # Check classes exist
        print(f"   ✅ RaceParser class exists")
        print(f"   ✅ ClassParser class exists")
        print(f"   ✅ RuleExtractor class exists")
        
        # Check methods exist
        extractor = RuleExtractor(Path("dummy"))
        has_methods = all(hasattr(extractor, method) for method in [
            'extract_all_rules'
        ])
        
        if has_methods:
            print(f"   ✅ All required methods exist")
            return True
        else:
            print(f"   ❌ Some methods missing")
            return False
        
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False


def run_all_tests():
    """Run all parser tests"""
    print("\n" + "="*70)
    print("KNOWLEDGE PARSER - TEST SUITE")
    print("="*70)
    
    tests = [
        ("Ability Scores Validation", test_ability_scores_validation),
        ("Character Creation Validation", test_character_creation_validation),
        ("Race Schema Validation", test_race_schema_validation),
        ("Class Schema Validation", test_class_schema_validation),
        ("Invalid Data Rejection", test_invalid_data_rejection),
        ("Immersive Parser Structure", test_immersive_parser_structure),
        ("Rule Parser Structure", test_rule_parser_structure)
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
