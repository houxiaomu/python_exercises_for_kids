"""
=== Exercise 0c: Sum of List (Without sum()) ===

TASK:
Calculate the TOTAL of all numbers in a list WITHOUT using the sum() function.
Use a loop to add each number one by one.

EXAMPLES:
[1, 2, 3]       ->  6
[10, 20, 30]    ->  60
[5]             ->  5
[]              ->  0
[-1, 1, -1, 1]  ->  0

HINT:
- Start with total = 0
- Use a for loop to go through each number
- Add each number to total
"""


def sum_list(numbers):
    """
    Calculate the sum of all numbers in the list (without using sum()).

    Args:
        numbers: a list of numbers
    Returns:
        The total sum (int or float)
    """
    # YOUR CODE HERE
    # DO NOT use sum()!
    total = 0

    return total


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing sum_list()...")
    print("-" * 40)

    tests = [
        ([1, 2, 3], 6),
        ([10, 20, 30], 60),
        ([5], 5),
        ([], 0),
        ([-1, 1, -1, 1], 0),
        ([1, 2, 3, 4, 5], 15),
        ([100, 200, 300], 600),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        result = sum_list(input_list)
        if result == expected:
            print(f"Test {i}: PASSED  sum of {input_list} is {result}")
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
