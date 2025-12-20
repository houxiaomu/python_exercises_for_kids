"""
=== Exercise 01: Reverse List (Without reverse() or [::-1]) ===

TASK:
Reverse a list WITHOUT using .reverse() or slicing [::-1].
Create a NEW list with elements in reverse order.

EXAMPLES:
[1, 2, 3, 4, 5]  ->  [5, 4, 3, 2, 1]
["a", "b", "c"]  ->  ["c", "b", "a"]
[7]             ->  [7]
[]              ->  []

HINT:
- Method 1: Start from the END of the list
  - Use range(len(items)-1, -1, -1) to go backwards
  - This gives you: 4, 3, 2, 1, 0 for a list of length 5

- Method 2: Insert at the beginning
  - Use result.insert(0, item) to add to the front
"""


def reverse_list(items):
    """
    Reverse the list (without using reverse() or [::-1]).

    Args:
        items: a list of any elements
    Returns:
        A new list with elements in reverse order
    """
    # YOUR CODE HERE
    # DO NOT use .reverse() or [::-1]!
    result = []

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing reverse_list()...")
    print("-" * 40)

    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (["a", "b", "c"], ["c", "b", "a"]),
        ([7], [7]),
        ([], []),
        ([1, 2], [2, 1]),
        ([10, 20, 30, 40], [40, 30, 20, 10]),
        (["hello", "world"], ["world", "hello"]),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        original = input_list.copy()
        result = reverse_list(input_list)

        if result == expected:
            print(f"Test {i}: PASSED  {original} -> {result}")
        else:
            print(f"Test {i}: FAILED  {original} -> {result} (expected {expected})")
            all_passed = False

        # Check that original list was not modified
        if input_list != original:
            print(f"  WARNING: You modified the original list!")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
