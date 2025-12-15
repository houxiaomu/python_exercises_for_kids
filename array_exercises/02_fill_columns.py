"""
=== Exercise 2: Fill Column by Column ===

TASK:
Create a 5x5 grid and fill it with numbers 0 to 24.
Fill from top to bottom, left to right (column by column).

EXAMPLE OUTPUT:
[[ 0,  5, 10, 15, 20],
 [ 1,  6, 11, 16, 21],
 [ 2,  7, 12, 17, 22],
 [ 3,  8, 13, 18, 23],
 [ 4,  9, 14, 19, 24]]

HINT:
- First create an empty grid filled with zeros
- Then use nested loops: outer for columns, inner for rows
- Formula: number = column * 5 + row
"""


def fill_columns(n=5):
    """
    Create an n x n grid filled with numbers 0 to n*n-1, column by column.

    Args:
        n: size of the grid (default 5)
    Returns:
        A 2D list (list of lists)
    """
    # YOUR CODE HERE
    # Step 1: Create an empty n x n grid filled with 0
    grid = []

    # Step 2: Fill the grid column by column

    return grid


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fill_columns()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_columns(5)
    expected = [
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24]
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
    result2 = fill_columns(3)
    expected2 = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

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
