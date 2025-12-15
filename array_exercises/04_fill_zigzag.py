"""
=== Exercise 4: Fill in Zigzag Pattern ===

TASK:
Create a 5x5 grid and fill it with numbers 0 to 24.
Fill in a zigzag pattern:
- Row 0: left to right (0, 1, 2, 3, 4)
- Row 1: right to left (9, 8, 7, 6, 5)
- Row 2: left to right (10, 11, 12, 13, 14)
- And so on...

EXAMPLE OUTPUT:
[[ 0,  1,  2,  3,  4],
 [ 9,  8,  7,  6,  5],
 [10, 11, 12, 13, 14],
 [19, 18, 17, 16, 15],
 [20, 21, 22, 23, 24]]

HINT:
- Check if row number is even or odd
- Even rows: fill left to right
- Odd rows: fill right to left
- Use: if row % 2 == 0  to check if row is even
"""


def fill_zigzag(n=5):
    """
    Create an n x n grid filled with numbers 0 to n*n-1 in zigzag pattern.

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
    print("Testing fill_zigzag()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_zigzag(5)
    expected = [
        [0, 1, 2, 3, 4],
        [9, 8, 7, 6, 5],
        [10, 11, 12, 13, 14],
        [19, 18, 17, 16, 15],
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

    # Test 2: 4x4 grid
    result2 = fill_zigzag(4)
    expected2 = [
        [0, 1, 2, 3],
        [7, 6, 5, 4],
        [8, 9, 10, 11],
        [15, 14, 13, 12]
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
