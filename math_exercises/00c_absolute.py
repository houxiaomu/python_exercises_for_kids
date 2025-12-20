"""
=== Exercise 00c: Absolute Value (Without abs()) ===

TASK:
Find the absolute value of a number WITHOUT using abs().
Absolute value is the "distance from zero" - always positive!

EXAMPLES:
5   ->  5
-5  ->  5
0   ->  0
-100 -> 100

HINT:
- If the number is negative, multiply by -1
- If the number is positive or zero, keep it the same
"""


def absolute(n):
    """
    Find the absolute value of n (without using abs()).

    Args:
        n: a number
    Returns:
        The absolute value (always >= 0)
    """
    # YOUR CODE HERE
    # DO NOT use abs()!
    return 0


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing absolute()...")
    print("-" * 40)

    tests = [
        (5, 5),
        (-5, 5),
        (0, 0),
        (-100, 100),
        (100, 100),
        (-1, 1),
        (42, 42),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = absolute(num)
        if result == expected:
            print(f"Test {i}: PASSED  |{num}| = {result}")
        else:
            print(f"Test {i}: FAILED  |{num}| -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
