"""
Master Test Runner - Executes all test suites
"""
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run_test_file(test_file: Path) -> bool:
    """
    Run a test file and return success status
    
    Args:
        test_file: Path to test file
        
    Returns:
        True if all tests passed
    """
    print(f"\n{'='*70}")
    print(f"Running: {test_file.name}")
    print(f"{'='*70}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(test_file)],
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running {test_file.name}: {e}")
        return False


def main():
    """Run all test suites"""
    print("\n" + "="*70)
    print("WHYTDD - MASTER TEST SUITE")
    print("="*70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get test directory
    test_dir = Path(__file__).parent
    
    # Test files to run (in order)
    test_files = [
        test_dir / "test_parsers.py",
        test_dir / "test_stats_calculator.py",
        test_dir / "test_behavioral_translator.py",
        test_dir / "test_character_creation.py"
    ]
    
    # Check all test files exist
    missing_files = [f for f in test_files if not f.exists()]
    if missing_files:
        print(f"\n❌ Missing test files:")
        for f in missing_files:
            print(f"   - {f.name}")
        sys.exit(1)
    
    print(f"\n📋 Found {len(test_files)} test suites")
    
    # Run each test suite
    results = []
    for test_file in test_files:
        success = run_test_file(test_file)
        results.append((test_file.name, success))
    
    # Final summary
    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, success in results if success)
    failed = len(results) - passed
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status}: {test_name}")
    
    print(f"\n{'='*70}")
    print(f"Total: {passed}/{len(results)} test suites passed")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}")
    
    if failed == 0:
        print("\n   🎉 ALL TEST SUITES PASSED! 🎉")
        print("\n   ✅ WhytDD is ready for Phase 4!")
        sys.exit(0)
    else:
        print(f"\n   ⚠️  {failed} test suite(s) failed")
        print("\n   Please fix failing tests before proceeding")
        sys.exit(1)


if __name__ == "__main__":
    main()
