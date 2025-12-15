"""
=== Exercise 5: Fill Diagonals ===

TASK:
Create a 5x5 grid and fill ONLY the two diagonals with 1, rest with 0.
Main diagonal: top-left to bottom-right
Anti-diagonal: top-right to bottom-left

EXAMPLE OUTPUT:
[[1, 0, 0, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 1, 0, 0],
 [0, 1, 0, 1, 0],
 [1, 0, 0, 0, 1]]

HINT:
- Main diagonal: row == column
- Anti-diagonal: row + column == n - 1
- Use these conditions to decide if a cell should be 1 or 0
"""


def fill_diagonal(n=5):
    """
    Create an n x n grid with 1s on both diagonals and 0s elsewhere.

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
    print("Testing fill_diagonal()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_diagonal(5)
    expected = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
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

    # Test 2: 4x4 grid
    result2 = fill_diagonal(4)
    expected2 = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ]

    if result2 == expected2:
        print("Test 2 (4x4): PASSED!")
    else:
        print("Test 2 (4x4): FAILED")
        return False

    print("-" * 40)
    print("ALL TESTS PASSED! Great job!")
    return True


if __name__ == "__main__":
    run_tests()
