"""
=== Exercise 0e: Fill Border Only ===

TASK:
Create a 5x5 grid where the border (edge) is 1 and inside is 0.

EXAMPLE OUTPUT:
[[1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1]]

HINT:
- A cell is on the border if:
  - row == 0 (top edge)
  - row == n-1 (bottom edge)
  - column == 0 (left edge)
  - column == n-1 (right edge)
- Use: if row == 0 or row == n-1 or col == 0 or col == n-1
"""


def fill_border(n=5):
    """
    Create an n x n grid with 1s on the border and 0s inside.

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
    print("Testing fill_border()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_border(5)
    expected = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
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
    result2 = fill_border(4)
    expected2 = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]

    if result2 == expected2:
        print("Test 2 (4x4): PASSED!")
    else:
        print("Test 2 (4x4): FAILED")
        return False

    # Test 3: 3x3 grid
    result3 = fill_border(3)
    expected3 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    if result3 == expected3:
        print("Test 3 (3x3): PASSED!")
    else:
        print("Test 3 (3x3): FAILED")
        return False

    print("-" * 40)
    print("ALL TESTS PASSED! Great job!")
    return True


if __name__ == "__main__":
    run_tests()
