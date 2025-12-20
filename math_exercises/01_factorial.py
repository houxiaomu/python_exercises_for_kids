"""
=== Exercise 01: Factorial ===

TASK:
Calculate the factorial of n.
Factorial means: n! = 1 × 2 × 3 × ... × n
Special case: 0! = 1

EXAMPLES:
5  ->  120  (1×2×3×4×5 = 120)
4  ->  24   (1×2×3×4 = 24)
3  ->  6    (1×2×3 = 6)
1  ->  1
0  ->  1    (special case!)

HINT:
- Start with result = 1
- Multiply by each number from 1 to n
- Use a for loop: for i in range(1, n+1)
"""


def factorial(n):
    """
    Calculate the factorial of n.

    Args:
        n: a non-negative integer
    Returns:
        n! (n factorial)
    """
    # YOUR CODE HERE
    result = 1

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing factorial()...")
    print("-" * 40)

    tests = [
        (5, 120),
        (4, 24),
        (3, 6),
        (2, 2),
        (1, 1),
        (0, 1),
        (6, 720),
        (7, 5040),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = factorial(num)
        if result == expected:
            print(f"Test {i}: PASSED  {num}! = {result}")
        else:
            print(f"Test {i}: FAILED  {num}! -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
