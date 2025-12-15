"""
=== Exercise 0b: Fill Each Row with Row Number ===

TASK:
Create a 5x5 grid where each row is filled with its row number.
Row 0 has all 0s, Row 1 has all 1s, etc.

EXAMPLE OUTPUT:
[[0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1],
 [2, 2, 2, 2, 2],
 [3, 3, 3, 3, 3],
 [4, 4, 4, 4, 4]]

HINT:
- Use two nested loops
- The value in each cell equals the row number
"""


def fill_row_number(n=5):
    """
    Create an n x n grid where each row is filled with its row number.

    Args:
        n: size of the grid (default 5)
    Returns:
        A 2D list (list of lists)
    """
    # YOUR CODE HERE
    grid = []

    return grid


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fill_row_number()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_row_number(5)
    expected = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]
    ]

    print("Your result:")
    for row in result:
        print(row)
    print()

    if result == expected:
        print("Test 1 (5x5): PASSED!")
    else:
        print("Test 1 (5x5): FAILED")
        print("Expected:")
        for row in expected:
            print(row)
        return False

    # Test 2: 3x3 grid
    result2 = fill_row_number(3)
    expected2 = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

    if result2 == expected2:
        print("Test 2 (3x3): PASSED!")
    else:
        print("Test 2 (3x3): FAILED")
        return False

    print("-" * 40)
    print("ALL TESTS PASSED! Great job!")
    return True


if __name__ == "__main__":
    run_tests()
