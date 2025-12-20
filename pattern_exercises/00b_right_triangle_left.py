"""
=== Exercise 00b: Right Triangle (Left-aligned) ===

TASK:
Print a right triangle that points to the LEFT.
Use '*' for stars and ' ' (space) for empty areas.

EXAMPLE (n=5):
    *
   **
  ***
 ****
*****

EXAMPLE (n=3):
  *
 **
***

HINT:
- Each row has: (n - row_number) spaces + (row_number) stars
- For row 1: 4 spaces + 1 star
- For row 5: 0 spaces + 5 stars
- Use ' ' * number for spaces
"""


def print_left_triangle(n):
    """
    Print a left-aligned right triangle with n rows.

    Args:
        n: number of rows
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_left_triangle()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_left_triangle(5)
    print()

    print("Test 2: n=3")
    print_left_triangle(3)
    print()

    print("Test 3: n=4")
    print_left_triangle(4)
    print()

    print("-" * 40)
    print("Check visually: Stars should align on the RIGHT side!")


if __name__ == "__main__":
    run_tests()
