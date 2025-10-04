"""
Tests for Stats Calculator Module
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from character_creator.stats_calculator import StatsManager, DiceRoller


def test_modifier_calculation():
    """Test ability score modifier calculation"""
    print("\n" + "="*70)
    print("TEST: Modifier Calculation")
    print("="*70)
    
    test_cases = [
        (1, -5),
        (3, -4),
        (8, -1),
        (10, 0),
        (12, 1),
        (15, 2),
        (18, 4),
        (20, 5),
        (30, 10)
    ]
    
    passed = 0
    failed = 0
    
    for score, expected_mod in test_cases:
        result = StatsManager.calculate_modifier(score)
        status = "✅" if result == expected_mod else "❌"
        print(f"   {status} Score {score:2d} → Modifier {result:+d} (expected {expected_mod:+d})")
        
        if result == expected_mod:
            passed += 1
        else:
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_standard_array():
    """Test standard array generation"""
    print("\n" + "="*70)
    print("TEST: Standard Array")
    print("="*70)
    
    array = StatsManager.get_standard_array()
    expected = [15, 14, 13, 12, 10, 8]
    
    if array == expected:
        print(f"   ✅ Standard array correct: {array}")
        return True
    else:
        print(f"   ❌ Standard array incorrect: {array}")
        print(f"      Expected: {expected}")
        return False


def test_point_buy_validation():
    """Test point buy validation"""
    print("\n" + "="*70)
    print("TEST: Point Buy Validation")
    print("="*70)
    
    test_cases = [
        ([15, 14, 13, 12, 10, 8], True, "Valid 27 points"),
        ([15, 15, 15, 8, 8, 8], True, "Valid 27 points (different distribution)"),
        ([15, 15, 15, 15, 8, 8], False, "Too many points (33)"),
        ([10, 10, 10, 10, 10, 10], False, "Too few points (12)"),
        ([16, 14, 13, 12, 10, 8], False, "Invalid score (16)"),
    ]
    
    passed = 0
    failed = 0
    
    for scores, should_be_valid, description in test_cases:
        is_valid, msg = StatsManager.validate_point_buy(scores)
        
        if is_valid == should_be_valid:
            print(f"   ✅ {description}: {is_valid}")
            passed += 1
        else:
            print(f"   ❌ {description}: {is_valid} (expected {should_be_valid})")
            print(f"      Message: {msg}")
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_racial_bonuses():
    """Test racial bonus application"""
    print("\n" + "="*70)
    print("TEST: Racial Bonus Application")
    print("="*70)
    
    base = {
        'Strength': 15,
        'Dexterity': 14,
        'Constitution': 13,
        'Intelligence': 12,
        'Wisdom': 10,
        'Charisma': 8
    }
    
    # Mountain Dwarf: +2 CON, +2 STR
    racial = {'Constitution': 2, 'Strength': 2}
    result = StatsManager.apply_racial_bonuses(base, racial)
    
    expected_str = 17
    expected_con = 15
    
    if result['Strength'] == expected_str and result['Constitution'] == expected_con:
        print(f"   ✅ Mountain Dwarf bonuses correct")
        print(f"      STR: {base['Strength']} → {result['Strength']} (+2)")
        print(f"      CON: {base['Constitution']} → {result['Constitution']} (+2)")
        return True
    else:
        print(f"   ❌ Mountain Dwarf bonuses incorrect")
        print(f"      STR: {result['Strength']} (expected {expected_str})")
        print(f"      CON: {result['Constitution']} (expected {expected_con})")
        return False


def test_dice_rolling():
    """Test dice rolling (statistical test)"""
    print("\n" + "="*70)
    print("TEST: Dice Rolling (100 rolls)")
    print("="*70)
    
    roller = DiceRoller()
    
    # Roll 100 times and check distribution
    rolls = []
    for _ in range(100):
        roll = roller.roll_4d6_drop_lowest()
        rolls.append(roll.total)
    
    min_roll = min(rolls)
    max_roll = max(rolls)
    avg_roll = sum(rolls) / len(rolls)
    
    # Expected: min=3, max=18, avg~12.24
    min_valid = 3 <= min_roll <= 8
    max_valid = 15 <= max_roll <= 18
    avg_valid = 10 <= avg_roll <= 14
    
    print(f"   Min: {min_roll} {'✅' if min_valid else '❌'} (expected 3-8)")
    print(f"   Max: {max_roll} {'✅' if max_valid else '❌'} (expected 15-18)")
    print(f"   Avg: {avg_roll:.2f} {'✅' if avg_valid else '❌'} (expected 10-14)")
    
    return min_valid and max_valid and avg_valid


def run_all_tests():
    """Run all stats calculator tests"""
    print("\n" + "="*70)
    print("STATS CALCULATOR - TEST SUITE")
    print("="*70)
    
    tests = [
        ("Modifier Calculation", test_modifier_calculation),
        ("Standard Array", test_standard_array),
        ("Point Buy Validation", test_point_buy_validation),
        ("Racial Bonuses", test_racial_bonuses),
        ("Dice Rolling", test_dice_rolling)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n   ❌ EXCEPTION: {e}")
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
