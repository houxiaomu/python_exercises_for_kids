"""
=== Exercise 0a: Fill with Same Number ===

TASK:
Create a 5x5 grid where ALL cells contain the same number.
The number should be the one passed to the function.

EXAMPLE (fill with 7):
[[7, 7, 7, 7, 7],
 [7, 7, 7, 7, 7],
 [7, 7, 7, 7, 7],
 [7, 7, 7, 7, 7],
 [7, 7, 7, 7, 7]]

HINT:
- Use two nested loops: one for rows, one for columns
- Each cell gets the same value
"""


def fill_same(n=5, value=0):
    """
    Create an n x n grid filled with the same value.

    Args:
        n: size of the grid (default 5)
        value: the number to fill (default 0)
    Returns:
        A 2D list (list of lists)
    """
    # YOUR CODE HERE
    grid = []

    return grid


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fill_same()...")
    print("-" * 40)

    # Test 1: 5x5 grid filled with 7
    result = fill_same(5, 7)
    expected = [
        [7, 7, 7, 7, 7],
        [7, 7, 7, 7, 7],
        [7, 7, 7, 7, 7],
        [7, 7, 7, 7, 7],
        [7, 7, 7, 7, 7]
    ]

    print("Your result (5x5 with 7):")
    for row in result:
        print(row)
    print()

    if result == expected:
        print("Test 1: PASSED!")
    else:
        print("Test 1: FAILED")
        return False

    # Test 2: 3x3 grid filled with 0
    result2 = fill_same(3, 0)
    expected2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    if result2 == expected2:
        print("Test 2 (3x3 with 0): PASSED!")
    else:
        print("Test 2 (3x3 with 0): FAILED")
        return False

    # Test 3: 4x4 grid filled with 99
    result3 = fill_same(4, 99)
    expected3 = [[99, 99, 99, 99]] * 4

    if result3 == expected3:
        print("Test 3 (4x4 with 99): PASSED!")
    else:
        print("Test 3 (4x4 with 99): FAILED")
        return False

    print("-" * 40)
    print("ALL TESTS PASSED! Great job!")
    return True


if __name__ == "__main__":
    run_tests()
