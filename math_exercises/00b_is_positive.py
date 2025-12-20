"""
=== Exercise 00b: Positive, Negative, or Zero ===

TASK:
Check if a number is positive, negative, or zero.
Return:
- "positive" if n > 0
- "negative" if n < 0
- "zero" if n == 0

EXAMPLES:
5   ->  "positive"
-3  ->  "negative"
0   ->  "zero"

HINT:
- Use if/elif/else
- Check the three cases: > 0, < 0, == 0
"""


def check_sign(n):
    """
    Check if n is positive, negative, or zero.

    Args:
        n: a number
    Returns:
        "positive", "negative", or "zero"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing check_sign()...")
    print("-" * 40)

    tests = [
        (5, "positive"),
        (-3, "negative"),
        (0, "zero"),
        (100, "positive"),
        (-100, "negative"),
        (1, "positive"),
        (-1, "negative"),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = check_sign(num)
        if result == expected:
            print(f"Test {i}: PASSED  {num} is {result}")
        else:
            print(f"Test {i}: FAILED  {num} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
