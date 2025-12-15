"""
=== Exercise 1: Fill Row by Row ===

TASK:
Create a 5x5 grid and fill it with numbers 0 to 24.
Fill from left to right, top to bottom.

EXAMPLE OUTPUT:
[[ 0,  1,  2,  3,  4],
 [ 5,  6,  7,  8,  9],
 [10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24]]

HINT:
- Use nested loops: outer loop for rows, inner loop for columns
- Formula: number = row * 5 + column
"""


def fill_rows(n=5):
    """
    Create an n x n grid filled with numbers 0 to n*n-1, row by row.

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
    print("Testing fill_rows()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_rows(5)
    expected = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24]
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
    result2 = fill_rows(3)
    expected2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

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
