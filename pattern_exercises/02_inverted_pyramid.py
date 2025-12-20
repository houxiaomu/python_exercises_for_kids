"""
=== Exercise 02: Inverted Pyramid ===

TASK:
Print an upside-down pyramid using '*' characters.

EXAMPLE (n=5):
*********
 *******
  *****
   ***
    *

EXAMPLE (n=3):
*****
 ***
  *

HINT:
- This is the opposite of a regular pyramid
- Row 1: 0 spaces + (2*n-1) stars
- Row 2: 1 space + (2*n-3) stars
- Pattern: spaces = row - 1, stars = 2*(n-row) + 1
"""


def print_inverted_pyramid(n):
    """
    Print an inverted pyramid with n rows.

    Args:
        n: number of rows
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_inverted_pyramid()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_inverted_pyramid(5)
    print()

    print("Test 2: n=3")
    print_inverted_pyramid(3)
    print()

    print("Test 3: n=4")
    print_inverted_pyramid(4)
    print()

    print("-" * 40)
    print("Check visually: Should be an upside-down pyramid!")


if __name__ == "__main__":
    run_tests()
