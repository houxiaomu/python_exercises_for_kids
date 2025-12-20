"""
=== Exercise 03: Diamond ===

TASK:
Print a diamond shape using '*' characters.
The diamond has n rows in the TOP HALF (including middle).

EXAMPLE (n=3):
  *
 ***
*****
 ***
  *

EXAMPLE (n=4):
   *
  ***
 *****
*******
 *****
  ***
   *

HINT:
- First, print a pyramid (top half)
- Then, print an inverted pyramid without the first row (bottom half)
- You can call your previous functions or write new loops
"""


def print_diamond(n):
    """
    Print a diamond with n rows in the top half.

    Args:
        n: number of rows in top half (including middle)
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_diamond()...")
    print("-" * 40)

    print("Test 1: n=3")
    print_diamond(3)
    print()

    print("Test 2: n=4")
    print_diamond(4)
    print()

    print("Test 3: n=5")
    print_diamond(5)
    print()

    print("-" * 40)
    print("Check visually: Should be a diamond shape!")


if __name__ == "__main__":
    run_tests()
