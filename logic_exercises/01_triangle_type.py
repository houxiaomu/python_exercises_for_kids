"""
=== Exercise 01: Triangle Type ===

TASK:
Given three sides of a triangle, determine its type:
- "equilateral": all 3 sides equal
- "isosceles": exactly 2 sides equal
- "scalene": all 3 sides different
- "invalid": cannot form a triangle

Triangle rule: sum of any 2 sides must be greater than the 3rd side.

EXAMPLES:
(3, 3, 3)  ->  "equilateral"
(3, 3, 4)  ->  "isosceles"
(3, 4, 5)  ->  "scalene"
(1, 1, 10) ->  "invalid"  (1+1 is NOT > 10)

HINT:
- First check if it's a valid triangle
- Then check: all equal? two equal? all different?
"""


def triangle_type(a, b, c):
    """
    Determine the type of triangle.

    Args:
        a, b, c: the three sides of the triangle
    Returns:
        "equilateral", "isosceles", "scalene", or "invalid"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing triangle_type()...")
    print("-" * 40)

    tests = [
        ((3, 3, 3), "equilateral"),
        ((5, 5, 5), "equilateral"),
        ((3, 3, 4), "isosceles"),
        ((4, 3, 3), "isosceles"),
        ((3, 4, 3), "isosceles"),
        ((3, 4, 5), "scalene"),
        ((5, 7, 9), "scalene"),
        ((1, 1, 10), "invalid"),
        ((1, 2, 3), "invalid"),
        ((0, 4, 4), "invalid"),
    ]

    all_passed = True
    for i, (sides, expected) in enumerate(tests, 1):
        a, b, c = sides
        result = triangle_type(a, b, c)
        if result == expected:
            print(f"Test {i}: PASSED  ({a},{b},{c}) is {result}")
        else:
            print(f"Test {i}: FAILED  ({a},{b},{c}) -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
