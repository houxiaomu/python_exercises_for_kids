"""
=== Exercise 0b: Find Minimum (Without min()) ===

TASK:
Find the SMALLEST number in a list WITHOUT using the min() function.
Use a loop to check each number one by one.

EXAMPLES:
[3, 1, 4, 1, 5]  ->  1
[10, 20, 30]    ->  10
[7]             ->  7
[-5, -1, -10]   ->  -10

HINT:
- Start by assuming the first number is the smallest
- Use a for loop to check each number
- If you find a smaller number, update your answer
"""


def find_min(numbers):
    """
    Find the smallest number in the list (without using min()).

    Args:
        numbers: a list of numbers (at least 1 number)
    Returns:
        The smallest number (int or float)
    """
    # YOUR CODE HERE
    # DO NOT use min()!
    smallest = None

    return smallest


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing find_min()...")
    print("-" * 40)

    tests = [
        ([3, 1, 4, 1, 5], 1),
        ([10, 20, 30], 10),
        ([7], 7),
        ([-5, -1, -10], -10),
        ([100, 50, 75, 25], 25),
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 1),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        result = find_min(input_list)
        if result == expected:
            print(f"Test {i}: PASSED  min of {input_list} is {result}")
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
