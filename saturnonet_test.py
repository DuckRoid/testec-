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
    print("✓ All add_numbers tests passed")


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(10, 10) == 100
    print("✓ All multiply_numbers tests passed")


def run_all_tests():
    """Run all test functions."""
    print("Running Saturnonet tests...")
    print("-" * 40)
    test_add_numbers()
    test_multiply_numbers()
    print("-" * 40)
    print("All tests passed successfully! ✓")


if __name__ == "__main__":
    run_all_tests()
