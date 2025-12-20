"""
=== Exercise 05: Sum of Digits ===

TASK:
Calculate the sum of all digits in a number.

EXAMPLES:
123   ->  6   (1 + 2 + 3 = 6)
456   ->  15  (4 + 5 + 6 = 15)
7     ->  7
1000  ->  1   (1 + 0 + 0 + 0 = 1)

HINT:
- Use n % 10 to get the last digit
- Use n // 10 to remove the last digit
- Keep doing this until n becomes 0
- Or convert to string and loop through each character
"""


def sum_digits(n):
    """
    Calculate the sum of all digits in n.

    Args:
        n: a non-negative integer
    Returns:
        The sum of all digits
    """
    # YOUR CODE HERE
    total = 0

    return total


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing sum_digits()...")
    print("-" * 40)

    tests = [
        (123, 6),
        (456, 15),
        (7, 7),
        (1000, 1),
        (9999, 36),
        (12345, 15),
        (0, 0),
        (111, 3),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = sum_digits(num)
        if result == expected:
            print(f"Test {i}: PASSED  sum of digits in {num} = {result}")
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
