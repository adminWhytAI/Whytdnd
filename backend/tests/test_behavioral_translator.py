"""
Tests for Behavioral Translator Module
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from character_creator.behavioral_translator import BehavioralProfileBuilder


def test_stat_translation():
    """Test stat-to-behavior translation"""
    print("\n" + "="*70)
    print("TEST: Stat Translation")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    # Test high STR, low CHA
    abilities = {
        'Strength': 18,
        'Dexterity': 10,
        'Constitution': 10,
        'Intelligence': 10,
        'Wisdom': 10,
        'Charisma': 8
    }
    
    directives = builder.translate_stats_to_behavior(abilities)
    
    # Check for high STR directives
    has_strength_directive = any('physically imposing' in d.lower() or 'powerful' in d.lower() 
                                  for d in directives)
    
    # Check for low CHA directives
    has_charisma_directive = any('struggle' in d.lower() or 'awkward' in d.lower() 
                                  for d in directives)
    
    print(f"   Abilities: STR 18, CHA 8")
    print(f"   Generated {len(directives)} directives")
    print(f"   ✅ Has high STR directive: {has_strength_directive}")
    print(f"   ✅ Has low CHA directive: {has_charisma_directive}")
    
    if directives:
        print(f"\n   Sample directives:")
        for directive in directives[:3]:
            print(f"      - {directive}")
    
    return has_strength_directive and has_charisma_directive and len(directives) > 0


def test_race_translation():
    """Test race-to-behavior translation"""
    print("\n" + "="*70)
    print("TEST: Race Translation")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    test_cases = [
        ('Dwarf', 'Mountain Dwarf', ['beard', 'clan', 'honor']),
        ('Elf', 'High Elf', ['centuries', 'grace', 'beauty']),
        ('Human', None, ['adaptable', 'ambitious', 'limited']),
    ]
    
    passed = 0
    failed = 0
    
    for race, subrace, keywords in test_cases:
        directives = builder.translate_race_to_behavior(race, subrace)
        
        # Check if at least one keyword is present
        has_keywords = any(
            any(keyword.lower() in directive.lower() for directive in directives)
            for keyword in keywords
        )
        
        if has_keywords and len(directives) > 0:
            print(f"   ✅ {race} ({subrace}): {len(directives)} directives")
            passed += 1
        else:
            print(f"   ❌ {race} ({subrace}): Missing expected keywords")
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_class_translation():
    """Test class-to-behavior translation"""
    print("\n" + "="*70)
    print("TEST: Class Translation")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    test_cases = [
        ('Fighter', ['disciplined', 'train', 'combat']),
        ('Wizard', ['intellectual', 'knowledge', 'arcane']),
        ('Rogue', ['observant', 'clever', 'instincts']),
        ('Cleric', ['faith', 'deity', 'compassion']),
    ]
    
    passed = 0
    failed = 0
    
    for class_name, keywords in test_cases:
        directives = builder.translate_class_to_behavior(class_name)
        
        # Check if at least one keyword is present
        has_keywords = any(
            any(keyword.lower() in directive.lower() for directive in directives)
            for keyword in keywords
        )
        
        if has_keywords and len(directives) > 0:
            print(f"   ✅ {class_name}: {len(directives)} directives")
            passed += 1
        else:
            print(f"   ❌ {class_name}: Missing expected keywords")
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_alignment_translation():
    """Test alignment-to-behavior translation"""
    print("\n" + "="*70)
    print("TEST: Alignment Translation")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    test_cases = [
        ('Lawful Good', ['honor', 'justice', 'word']),
        ('Chaotic Good', ['conscience', 'freedom', 'rebel']),
        ('Neutral Evil', ['benefit', 'self', 'pragmatic']),
    ]
    
    passed = 0
    failed = 0
    
    for alignment, keywords in test_cases:
        directives = builder.translate_alignment_to_behavior(alignment)
        
        # Check if at least one keyword is present
        has_keywords = any(
            any(keyword.lower() in directive.lower() for directive in directives)
            for keyword in keywords
        )
        
        if has_keywords and len(directives) > 0:
            print(f"   ✅ {alignment}: {len(directives)} directives")
            passed += 1
        else:
            print(f"   ❌ {alignment}: Missing expected keywords")
            failed += 1
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    return failed == 0


def test_complete_profile():
    """Test complete profile building"""
    print("\n" + "="*70)
    print("TEST: Complete Profile Building")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    # Bruenor Battlehammer
    abilities = {
        'Strength': 17,
        'Dexterity': 12,
        'Constitution': 17,
        'Intelligence': 10,
        'Wisdom': 13,
        'Charisma': 8
    }
    
    profile = builder.build_complete_profile(
        abilities=abilities,
        race="Dwarf",
        class_name="Fighter",
        alignment="Lawful Good",
        subrace="Mountain Dwarf",
        personality_traits=["I am always polite and respectful"]
    )
    
    print(f"   Character: Mountain Dwarf Fighter (Lawful Good)")
    print(f"   Total directives: {profile['total_directives']}")
    print(f"   Breakdown:")
    print(f"      - Stats: {len(profile['stat_behaviors'])}")
    print(f"      - Race: {len(profile['racial_behaviors'])}")
    print(f"      - Class: {len(profile['class_behaviors'])}")
    print(f"      - Alignment: {len(profile['alignment_behaviors'])}")
    print(f"      - Custom: {len(profile['custom_traits'])}")
    
    # Validate structure
    has_all_categories = all(key in profile for key in [
        'stat_behaviors', 'racial_behaviors', 'class_behaviors',
        'alignment_behaviors', 'all_directives', 'total_directives'
    ])
    
    has_reasonable_count = 20 <= profile['total_directives'] <= 50
    
    if has_all_categories and has_reasonable_count:
        print(f"\n   ✅ Profile structure valid")
        print(f"   ✅ Directive count reasonable ({profile['total_directives']})")
        
        print(f"\n   Sample directives:")
        for i, directive in enumerate(profile['all_directives'][:5], 1):
            print(f"      {i}. {directive}")
        
        return True
    else:
        print(f"\n   ❌ Profile validation failed")
        if not has_all_categories:
            print(f"      Missing categories")
        if not has_reasonable_count:
            print(f"      Unreasonable directive count: {profile['total_directives']}")
        return False


def run_all_tests():
    """Run all behavioral translator tests"""
    print("\n" + "="*70)
    print("BEHAVIORAL TRANSLATOR - TEST SUITE")
    print("="*70)
    
    tests = [
        ("Stat Translation", test_stat_translation),
        ("Race Translation", test_race_translation),
        ("Class Translation", test_class_translation),
        ("Alignment Translation", test_alignment_translation),
        ("Complete Profile", test_complete_profile)
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
