"""
=== Exercise 04: Greatest Common Divisor (GCD) ===

TASK:
Find the Greatest Common Divisor (GCD) of two numbers.
GCD is the largest number that divides both numbers evenly.

EXAMPLES:
12, 8   ->  4   (4 divides both 12 and 8)
15, 5   ->  5   (5 divides both 15 and 5)
7, 3    ->  1   (only 1 divides both)
20, 20  ->  20

HINT - Method 1 (Simple):
- Try all numbers from 1 to min(a, b)
- Keep track of the largest one that divides both

HINT - Method 2 (Euclidean algorithm):
- While b != 0: a, b = b, a % b
- Return a
"""


def gcd(a, b):
    """
    Find the greatest common divisor of a and b.

    Args:
        a: a positive integer
        b: a positive integer
    Returns:
        The GCD of a and b
    """
    # YOUR CODE HERE
    return 1


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing gcd()...")
    print("-" * 40)

    tests = [
        ((12, 8), 4),
        ((15, 5), 5),
        ((7, 3), 1),
        ((20, 20), 20),
        ((48, 18), 6),
        ((100, 25), 25),
        ((17, 13), 1),
        ((36, 24), 12),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        a, b = inputs
        result = gcd(a, b)
        if result == expected:
            print(f"Test {i}: PASSED  gcd({a}, {b}) = {result}")
        else:
            print(f"Test {i}: FAILED  gcd({a}, {b}) -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
