"""
=== Exercise 02: Remove Duplicates (Without set()) ===

TASK:
Remove duplicate numbers from a list WITHOUT using set().
Keep only the FIRST occurrence of each number.
The order should stay the same.

EXAMPLES:
[1, 2, 2, 3, 3, 3]  ->  [1, 2, 3]
[5, 5, 5, 5]        ->  [5]
[1, 2, 3]           ->  [1, 2, 3]  (no duplicates)
[]                  ->  []
[3, 1, 3, 2, 1]     ->  [3, 1, 2]  (keep first occurrence)

HINT:
- Create a new empty list for results
- For each number, check if it's ALREADY in your result list
- If NOT in result, add it
- You can use 'in' to check: if num not in result
"""


def remove_duplicates(numbers):
    """
    Remove duplicate numbers from the list (without using set()).

    Args:
        numbers: a list of numbers (may have duplicates)
    Returns:
        A new list with duplicates removed
    """
    # YOUR CODE HERE
    # DO NOT use set()!
    result = []

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing remove_duplicates()...")
    print("-" * 40)

    tests = [
        ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
        ([5, 5, 5, 5], [5]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([3, 1, 3, 2, 1], [3, 1, 2]),
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
        ([7], [7]),
        ([1, 2, 1, 2, 1, 2], [1, 2]),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        original = input_list.copy()
        result = remove_duplicates(input_list)

        if result == expected:
            print(f"Test {i}: PASSED  {original} -> {result}")
        else:
            print(f"Test {i}: FAILED  {original} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
