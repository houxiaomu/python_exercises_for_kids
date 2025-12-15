"""
=== Exercise 3: Fill in Reverse Order ===

TASK:
Create a 5x5 grid and fill it with numbers 0 to 24.
Fill from right to left, bottom to top (reverse order).

EXAMPLE OUTPUT:
[[24, 23, 22, 21, 20],
 [19, 18, 17, 16, 15],
 [14, 13, 12, 11, 10],
 [ 9,  8,  7,  6,  5],
 [ 4,  3,  2,  1,  0]]

HINT:
- You can start from the last row and last column
- Or fill normally and then calculate: number = 24 - (row * 5 + column)
"""


def fill_reverse(n=5):
    """
    Create an n x n grid filled with numbers 0 to n*n-1 in reverse order.

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
    print("Testing fill_reverse()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_reverse(5)
    expected = [
        [24, 23, 22, 21, 20],
        [19, 18, 17, 16, 15],
        [14, 13, 12, 11, 10],
        [9, 8, 7, 6, 5],
        [4, 3, 2, 1, 0]
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
    result2 = fill_reverse(3)
    expected2 = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]

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
