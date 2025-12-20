"""
=== Exercise 03: Count Each Number ===

TASK:
Count how many times EACH number appears in a list.
Return a dictionary where:
- Keys are the numbers
- Values are how many times each number appears

EXAMPLES:
[1, 2, 2, 3, 3, 3]  ->  {1: 1, 2: 2, 3: 3}
[5, 5, 5]          ->  {5: 3}
[1, 2, 3]          ->  {1: 1, 2: 1, 3: 1}
[]                 ->  {}
[7, 7, 8, 7, 8]    ->  {7: 3, 8: 2}

HINT:
- Create an empty dictionary: counts = {}
- For each number in the list:
  - If the number is already a key, add 1 to its value
  - If the number is NOT a key, set its value to 1
- Use: if num in counts  OR  if num not in counts
"""


def count_each(numbers):
    """
    Count how many times each number appears.

    Args:
        numbers: a list of numbers
    Returns:
        A dictionary with numbers as keys and counts as values
    """
    # YOUR CODE HERE
    counts = {}

    return counts


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing count_each()...")
    print("-" * 40)

    tests = [
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}),
        ([5, 5, 5], {5: 3}),
        ([1, 2, 3], {1: 1, 2: 1, 3: 1}),
        ([], {}),
        ([7, 7, 8, 7, 8], {7: 3, 8: 2}),
        ([1], {1: 1}),
        ([1, 1, 1, 1], {1: 4}),
        ([10, 20, 10, 30, 20, 10], {10: 3, 20: 2, 30: 1}),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        result = count_each(input_list)

        if result == expected:
            print(f"Test {i}: PASSED  {input_list} -> {result}")
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
