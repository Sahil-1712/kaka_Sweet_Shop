import unittest
import sys
from io import StringIO


def run_tests_with_report():
    """Run tests and generate a detailed report."""
    # Capture test output
    test_output = StringIO()
    runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    result = runner.run(suite)
    
    # Get the output
    output = test_output.getvalue()
    
    # Print results
    print("=" * 70)
    print("SWEET SHOP MANAGEMENT SYSTEM - TEST REPORT")
    print("=" * 70)
    print(output)
    
    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    print("=" * 70)
    
    # Return success status
    return len(result.failures) == 0 and len(result.errors) == 0


if __name__ == '__main__':
    success = run_tests_with_report()
    sys.exit(0 if success else 1)