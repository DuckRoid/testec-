#!/usr/bin/env python3
"""
Test script for Saturnonet functionality
This is a simple test demonstrating basic testing capabilities.
"""


def add_numbers(a, b):
    """Add two numbers together."""
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers together."""
    return a * b


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5
    return "✓ All add_numbers tests passed"


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(10, 10) == 100
    return "✓ All multiply_numbers tests passed"


def run_all_tests():
    """Run all test functions."""
    print("Running Saturnonet tests...")
    print("-" * 40)
    
    tests = [test_add_numbers, test_multiply_numbers]
    results = []
    
    for test_func in tests:
        try:
            result = test_func()
            results.append((test_func.__name__, True, result))
            print(result)
        except AssertionError as e:
            results.append((test_func.__name__, False, str(e)))
            print(f"✗ {test_func.__name__} failed: {e}")
    
    print("-" * 40)
    
    failed = [r for r in results if not r[1]]
    if failed:
        print(f"Tests failed: {len(failed)}/{len(results)}")
        return False
    else:
        print("All tests passed successfully! ✓")
        return True


if __name__ == "__main__":
    run_all_tests()
