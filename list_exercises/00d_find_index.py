"""
=== Exercise 0d: Find Index (Without .index()) ===

TASK:
Find the POSITION (index) of a number in a list WITHOUT using .index().
If the number is not in the list, return -1.
Remember: in Python, the first position is 0, not 1!

EXAMPLES:
[10, 20, 30, 40], 30  ->  2   (30 is at position 2)
[10, 20, 30, 40], 10  ->  0   (10 is at position 0)
[10, 20, 30, 40], 50  ->  -1  (50 is not in the list)
[5, 5, 5], 5          ->  0   (return the FIRST position)

HINT:
- Use a loop with range(len(numbers))
- This gives you the index: 0, 1, 2, 3...
- Check if numbers[i] equals the target
"""


def find_index(numbers, target):
    """
    Find the index of target in the list (without using .index()).

    Args:
        numbers: a list of numbers
        target: the number to find
    Returns:
        The index of target, or -1 if not found
    """
    # YOUR CODE HERE
    # DO NOT use .index()!

    return -1


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing find_index()...")
    print("-" * 40)

    tests = [
        (([10, 20, 30, 40], 30), 2),
        (([10, 20, 30, 40], 10), 0),
        (([10, 20, 30, 40], 40), 3),
        (([10, 20, 30, 40], 50), -1),
        (([5, 5, 5], 5), 0),
        (([1, 2, 3, 4, 5], 3), 2),
        (([], 5), -1),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        numbers, target = inputs
        result = find_index(numbers, target)
        if result == expected:
            print(f"Test {i}: PASSED  index of {target} in {numbers} is {result}")
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
