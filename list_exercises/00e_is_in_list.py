"""
=== Exercise 0e: Is In List (Without 'in' keyword) ===

TASK:
Check if a number EXISTS in a list WITHOUT using the 'in' keyword.
Return True if found, False if not found.

EXAMPLES:
[1, 2, 3, 4, 5], 3  ->  True   (3 is in the list)
[1, 2, 3, 4, 5], 6  ->  False  (6 is NOT in the list)
[], 5               ->  False  (empty list has nothing)
[7, 7, 7], 7        ->  True

HINT:
- Use a for loop to check each number
- If you find the target, return True immediately
- If the loop finishes without finding it, return False
"""


def is_in_list(numbers, target):
    """
    Check if target is in the list (without using 'in' keyword).

    Args:
        numbers: a list of numbers
        target: the number to find
    Returns:
        True if found, False otherwise
    """
    # YOUR CODE HERE
    # DO NOT use 'in'! (like: target in numbers)

    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing is_in_list()...")
    print("-" * 40)

    tests = [
        (([1, 2, 3, 4, 5], 3), True),
        (([1, 2, 3, 4, 5], 6), False),
        (([], 5), False),
        (([7, 7, 7], 7), True),
        (([10, 20, 30], 20), True),
        (([10, 20, 30], 15), False),
        (([0], 0), True),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        numbers, target = inputs
        result = is_in_list(numbers, target)
        if result == expected:
            status = "found" if result else "not found"
            print(f"Test {i}: PASSED  {target} {status} in {numbers}")
        else:
            print(f"Test {i}: FAILED  {numbers}, {target} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
