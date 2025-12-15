"""
=== Exercise 6: Fill in Spiral Pattern (Challenge!) ===

TASK:
Create a 5x5 grid and fill it with numbers 0 to 24 in a spiral pattern.
Start from top-left, go right, then down, then left, then up, and repeat.

EXAMPLE OUTPUT:
[[ 0,  1,  2,  3,  4],
 [15, 16, 17, 18,  5],
 [14, 23, 24, 19,  6],
 [13, 22, 21, 20,  7],
 [12, 11, 10,  9,  8]]

HINT:
- Keep track of boundaries: top, bottom, left, right
- Fill one edge at a time, then shrink the boundary
- Direction order: right -> down -> left -> up -> repeat

STEP BY STEP:
1. Fill top row (left to right), then move top boundary down
2. Fill right column (top to bottom), then move right boundary left
3. Fill bottom row (right to left), then move bottom boundary up
4. Fill left column (bottom to top), then move left boundary right
5. Repeat until all cells are filled
"""


def fill_spiral(n=5):
    """
    Create an n x n grid filled with numbers 0 to n*n-1 in spiral pattern.

    Args:
        n: size of the grid (default 5)
    Returns:
        A 2D list (list of lists)
    """
    # YOUR CODE HERE
    # Step 1: Create an n x n grid filled with 0
    grid = [[0] * n for _ in range(n)]

    # Step 2: Set up boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    # Step 3: Fill the spiral
    num = 0

    # Keep going while there are cells to fill
    while num < n * n:
        # Fill top row (left to right)

        # Fill right column (top to bottom)

        # Fill bottom row (right to left)

        # Fill left column (bottom to top)

        pass  # Remove this line when you add your code

    return grid


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fill_spiral()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_spiral(5)
    expected = [
        [0, 1, 2, 3, 4],
        [15, 16, 17, 18, 5],
        [14, 23, 24, 19, 6],
        [13, 22, 21, 20, 7],
        [12, 11, 10, 9, 8]
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
    result2 = fill_spiral(4)
    expected2 = [
        [0, 1, 2, 3],
        [11, 12, 13, 4],
        [10, 15, 14, 5],
        [9, 8, 7, 6]
    ]

    if result2 == expected2:
        print("Test 2 (4x4): PASSED!")
    else:
        print("Test 2 (4x4): FAILED")
        return False

    # Test 3: 3x3 grid
    result3 = fill_spiral(3)
    expected3 = [
        [0, 1, 2],
        [7, 8, 3],
        [6, 5, 4]
    ]

    if result3 == expected3:
        print("Test 3 (3x3): PASSED!")
    else:
        print("Test 3 (3x3): FAILED")
        return False

    print("-" * 40)
    print("ALL TESTS PASSED! Amazing work! You are a spiral master!")
    return True


if __name__ == "__main__":
    run_tests()
