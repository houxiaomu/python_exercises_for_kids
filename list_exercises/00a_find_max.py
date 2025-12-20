"""
=== Exercise 0a: Find Maximum (Without max()) ===

TASK:
Find the LARGEST number in a list WITHOUT using the max() function.
Use a loop to check each number one by one.

EXAMPLES:
[3, 1, 4, 1, 5]  ->  5
[10, 20, 30]    ->  30
[7]             ->  7
[-5, -1, -10]   ->  -1

HINT:
- Start by assuming the first number is the largest
- Use a for loop to check each number
- If you find a bigger number, update your answer
"""


def find_max(numbers):
    """
    Find the largest number in the list (without using max()).

    Args:
        numbers: a list of numbers (at least 1 number)
    Returns:
        The largest number (int or float)
    """
    # YOUR CODE HERE
    # DO NOT use max()!
    largest = None

    return largest


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing find_max()...")
    print("-" * 40)

    tests = [
        ([3, 1, 4, 1, 5], 5),
        ([10, 20, 30], 30),
        ([7], 7),
        ([-5, -1, -10], -1),
        ([100, 50, 75, 100], 100),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        result = find_max(input_list)
        if result == expected:
            print(f"Test {i}: PASSED  max of {input_list} is {result}")
        else:
            print(f"Test {i}: FAILED  {input_list} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
