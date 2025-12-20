"""
=== Exercise 03: Fibonacci Sequence ===

TASK:
Generate the first n numbers in the Fibonacci sequence.
Fibonacci: each number is the sum of the two before it.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

EXAMPLES:
5  ->  [0, 1, 1, 2, 3]
7  ->  [0, 1, 1, 2, 3, 5, 8]
1  ->  [0]
2  ->  [0, 1]

HINT:
- Start with [0, 1]
- Each new number = last number + second-to-last number
- Use a loop to add new numbers until you have n numbers
"""


def fibonacci(n):
    """
    Generate the first n Fibonacci numbers.

    Args:
        n: how many numbers to generate (n >= 1)
    Returns:
        A list of the first n Fibonacci numbers
    """
    # YOUR CODE HERE
    if n <= 0:
        return []

    result = []

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fibonacci()...")
    print("-" * 40)

    tests = [
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = fibonacci(num)
        if result == expected:
            print(f"Test {i}: PASSED  first {num} Fibonacci: {result}")
        else:
            print(f"Test {i}: FAILED  first {num} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
