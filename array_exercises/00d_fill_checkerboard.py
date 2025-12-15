"""
=== Exercise 0d: Fill Checkerboard Pattern ===

TASK:
Create a 5x5 grid with a checkerboard pattern (like a chess board).
Use 0 and 1 alternating.
Start with 0 at position [0][0].

EXAMPLE OUTPUT:
[[0, 1, 0, 1, 0],
 [1, 0, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [1, 0, 1, 0, 1],
 [0, 1, 0, 1, 0]]

HINT:
- Look at row + column: if the sum is even, use 0; if odd, use 1
- Use: (row + column) % 2 to get 0 or 1
"""


def fill_checkerboard(n=5):
    """
    Create an n x n checkerboard pattern with 0s and 1s.

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
    print("Testing fill_checkerboard()...")
    print("-" * 40)

    # Test 1: 5x5 grid
    result = fill_checkerboard(5)
    expected = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
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
    result2 = fill_checkerboard(4)
    expected2 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
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
