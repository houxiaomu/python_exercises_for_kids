"""
=== Exercise 04: Hollow Square ===

TASK:
Print a hollow square - only the border has '*', inside is empty.

EXAMPLE (n=5):
*****
*   *
*   *
*   *
*****

EXAMPLE (n=4):
****
*  *
*  *
****

HINT:
- First and last row: all stars
- Middle rows: star + spaces + star
- Middle rows have (n-2) spaces inside
"""


def print_hollow_square(n):
    """
    Print a hollow square with n rows and n columns.

    Args:
        n: size of the square
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_hollow_square()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_hollow_square(5)
    print()

    print("Test 2: n=4")
    print_hollow_square(4)
    print()

    print("Test 3: n=6")
    print_hollow_square(6)
    print()

    print("-" * 40)
    print("Check visually: Should be a hollow square (border only)!")


if __name__ == "__main__":
    run_tests()
