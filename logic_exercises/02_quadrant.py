"""
=== Exercise 02: Coordinate Quadrant ===

TASK:
Given x and y coordinates, determine which quadrant the point is in.

         |
    II   |   I
         |
  -------+-------
         |
   III   |   IV
         |

- Quadrant I:   x > 0, y > 0
- Quadrant II:  x < 0, y > 0
- Quadrant III: x < 0, y < 0
- Quadrant IV:  x > 0, y < 0
- On axis: x = 0 or y = 0 -> return "axis"

EXAMPLES:
(3, 4)   ->  1
(-2, 5)  ->  2
(-1, -1) ->  3
(4, -2)  ->  4
(0, 5)   ->  "axis"
(3, 0)   ->  "axis"

HINT:
- First check if on an axis (x=0 or y=0)
- Then use if/elif to check each quadrant
"""


def get_quadrant(x, y):
    """
    Determine which quadrant the point (x, y) is in.

    Args:
        x: the x-coordinate
        y: the y-coordinate
    Returns:
        1, 2, 3, 4 for quadrants, or "axis" if on an axis
    """
    # YOUR CODE HERE
    return 0


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing get_quadrant()...")
    print("-" * 40)

    tests = [
        ((3, 4), 1),
        ((1, 1), 1),
        ((-2, 5), 2),
        ((-1, 1), 2),
        ((-1, -1), 3),
        ((-5, -5), 3),
        ((4, -2), 4),
        ((1, -1), 4),
        ((0, 5), "axis"),
        ((3, 0), "axis"),
        ((0, 0), "axis"),
    ]

    all_passed = True
    for i, (coords, expected) in enumerate(tests, 1):
        x, y = coords
        result = get_quadrant(x, y)
        if result == expected:
            print(f"Test {i}: PASSED  ({x}, {y}) is in quadrant {result}")
        else:
            print(f"Test {i}: FAILED  ({x}, {y}) -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
