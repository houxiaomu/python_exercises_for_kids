"""
=== Exercise 00a: Leap Year ===

TASK:
Check if a year is a LEAP YEAR.
Leap year rules:
1. Divisible by 4 -> leap year
2. BUT if divisible by 100 -> NOT leap year
3. UNLESS also divisible by 400 -> leap year

EXAMPLES:
2024  ->  True   (divisible by 4)
2000  ->  True   (divisible by 400)
1900  ->  False  (divisible by 100 but not 400)
2023  ->  False  (not divisible by 4)

HINT:
- Check divisibility using %
- Order matters! Check 400 first, then 100, then 4
- Or use: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
"""


def is_leap_year(year):
    """
    Check if year is a leap year.

    Args:
        year: a year (integer)
    Returns:
        True if leap year, False otherwise
    """
    # YOUR CODE HERE
    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing is_leap_year()...")
    print("-" * 40)

    tests = [
        (2024, True),
        (2023, False),
        (2000, True),
        (1900, False),
        (2020, True),
        (2100, False),
        (2400, True),
        (1996, True),
    ]

    all_passed = True
    for i, (year, expected) in enumerate(tests, 1):
        result = is_leap_year(year)
        status = "leap year" if result else "not leap year"
        if result == expected:
            print(f"Test {i}: PASSED  {year} is {status}")
        else:
            print(f"Test {i}: FAILED  {year} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
