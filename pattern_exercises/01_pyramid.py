"""
=== Exercise 01: Pyramid ===

TASK:
Print a pyramid (centered triangle) using '*' characters.

EXAMPLE (n=5):
    *
   ***
  *****
 *******
*********

EXAMPLE (n=3):
  *
 ***
*****

HINT:
- Row 1: (n-1) spaces + 1 star
- Row 2: (n-2) spaces + 3 stars
- Row 3: (n-3) spaces + 5 stars
- Pattern: spaces = n - row, stars = 2*row - 1
"""


def print_pyramid(n):
    """
    Print a pyramid with n rows.

    Args:
        n: number of rows
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_pyramid()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_pyramid(5)
    print()

    print("Test 2: n=3")
    print_pyramid(3)
    print()

    print("Test 3: n=4")
    print_pyramid(4)
    print()

    print("-" * 40)
    print("Check visually: Should be a centered pyramid!")


if __name__ == "__main__":
    run_tests()
