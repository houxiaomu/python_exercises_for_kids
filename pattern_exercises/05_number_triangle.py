"""
=== Exercise 05: Number Triangle ===

TASK:
Print a triangle using numbers instead of stars.
Each row shows numbers from 1 to the row number.

EXAMPLE (n=5):
1
12
123
1234
12345

EXAMPLE (n=3):
1
12
123

HINT:
- Row 1: print "1"
- Row 2: print "12"
- Row 3: print "123"
- Build a string by adding numbers in a loop
"""


def print_number_triangle(n):
    """
    Print a number triangle with n rows.

    Args:
        n: number of rows
    Returns:
        None (just prints)
    """
    # YOUR CODE HERE
    pass


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing print_number_triangle()...")
    print("-" * 40)

    print("Test 1: n=5")
    print_number_triangle(5)
    print()

    print("Test 2: n=3")
    print_number_triangle(3)
    print()

    print("Test 3: n=9")
    print_number_triangle(9)
    print()

    print("-" * 40)
    print("Check visually: Each row should show 1,2,3... up to row number!")


if __name__ == "__main__":
    run_tests()
