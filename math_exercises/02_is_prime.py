"""
=== Exercise 02: Is Prime ===

TASK:
Check if a number is a PRIME number.
A prime number is only divisible by 1 and itself.
Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23...

EXAMPLES:
7   ->  True   (only divisible by 1 and 7)
4   ->  False  (divisible by 2)
2   ->  True   (smallest prime)
1   ->  False  (1 is NOT prime)
0   ->  False

HINT:
- Numbers less than 2 are NOT prime
- Check if any number from 2 to n-1 divides n evenly
- If n % i == 0 for any i, it's NOT prime
- Optimization: only check up to sqrt(n), but checking to n works too
"""


def is_prime(n):
    """
    Check if n is a prime number.

    Args:
        n: an integer
    Returns:
        True if prime, False otherwise
    """
    # YOUR CODE HERE
    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing is_prime()...")
    print("-" * 40)

    tests = [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (1, False),
        (0, False),
        (11, True),
        (12, False),
        (17, True),
        (25, False),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = is_prime(num)
        status = "prime" if result else "not prime"
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
