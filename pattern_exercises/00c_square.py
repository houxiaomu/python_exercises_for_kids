"""
=== Exercise 00c: Square ===

TASK:
Print a square of '*' characters with n rows and n columns.

EXAMPLE (n=4):
****
****
****
****

EXAMPLE (n=3):
***
***
***

HINT:
- Use a loop for rows (n times)
- Each row prints n stars
- '*' * n gives you n stars
"""


def print_square(n):
    """
    Print a square with n rows and n columns.

    Args:
        n: size of the square
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_square()...")
    print("-" * 40)

    print("Test 1: n=4")
    print_square(4)
    print()

    print("Test 2: n=3")
    print_square(3)
    print()

    print("Test 3: n=5")
    print_square(5)
    print()

    print("-" * 40)
    print("Check visually: Should be a square shape!")


if __name__ == "__main__":
    run_tests()
