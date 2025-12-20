"""
=== Exercise 00a: Right Triangle (Right-aligned) ===

TASK:
Print a right triangle using '*' characters.
The triangle should have n rows.

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
- Use a loop from 1 to n
- In each row, print that many '*' characters
- You can use '*' * number to repeat characters
"""


def print_right_triangle(n):
    """
    Print a right triangle with n rows.

    Args:
        n: number of rows
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_right_triangle()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_right_triangle(5)
    print()

    print("Test 2: n=3")
    print_right_triangle(3)
    print()

    print("Test 3: n=1")
    print_right_triangle(1)
    print()

    print("-" * 40)
    print("Check visually: Does it look correct?")
    print("Row 1 should have 1 star, Row 2 should have 2 stars, etc.")


if __name__ == "__main__":
    run_tests()
