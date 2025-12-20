"""
=== Exercise 00a: Is Even or Odd ===

TASK:
Check if a number is EVEN or ODD.
- Even numbers: 0, 2, 4, 6, 8, 10...
- Odd numbers: 1, 3, 5, 7, 9, 11...

EXAMPLES:
4   ->  True  (even)
7   ->  False (odd)
0   ->  True  (even)
-2  ->  True  (even)

HINT:
- A number is even if it divides by 2 with no remainder
- Use the modulo operator: n % 2
- If n % 2 == 0, the number is even
"""


def is_even(n):
    """
    Check if n is an even number.

    Args:
        n: an integer
    Returns:
        True if even, False if odd
    """
    # YOUR CODE HERE
    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing is_even()...")
    print("-" * 40)

    tests = [
        (4, True),
        (7, False),
        (0, True),
        (-2, True),
        (-3, False),
        (100, True),
        (99, False),
        (1, False),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = is_even(num)
        status = "even" if result else "odd"
        if result == expected:
            print(f"Test {i}: PASSED  {num} is {status}")
        else:
            print(f"Test {i}: FAILED  {num} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
