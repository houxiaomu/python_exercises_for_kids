"""
=== Exercise 0f: Double All Numbers ===

TASK:
Create a NEW list where every number is DOUBLED (multiplied by 2).
Do NOT change the original list!

EXAMPLES:
[1, 2, 3]     ->  [2, 4, 6]
[5, 10, 15]   ->  [10, 20, 30]
[0, 1, 0]     ->  [0, 2, 0]
[]            ->  []

HINT:
- Create a new empty list: result = []
- Use a for loop to go through each number
- Multiply each number by 2 and add to result
- Use result.append() to add numbers
"""


def double_all(numbers):
    """
    Create a new list with all numbers doubled.

    Args:
        numbers: a list of numbers
    Returns:
        A new list with each number multiplied by 2
    """
    # YOUR CODE HERE
    result = []

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing double_all()...")
    print("-" * 40)

    tests = [
        ([1, 2, 3], [2, 4, 6]),
        ([5, 10, 15], [10, 20, 30]),
        ([0, 1, 0], [0, 2, 0]),
        ([], []),
        ([100], [200]),
        ([-1, -2, -3], [-2, -4, -6]),
        ([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]),
    ]

    all_passed = True
    for i, (input_list, expected) in enumerate(tests, 1):
        original = input_list.copy()  # Save original
        result = double_all(input_list)

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
