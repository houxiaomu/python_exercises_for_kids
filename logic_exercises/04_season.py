"""
=== Exercise 04: What Season ===

TASK:
Given a month number (1-12), return the season.
- Spring: March, April, May (3, 4, 5)
- Summer: June, July, August (6, 7, 8)
- Fall:   September, October, November (9, 10, 11)
- Winter: December, January, February (12, 1, 2)

EXAMPLES:
1   ->  "Winter"
4   ->  "Spring"
7   ->  "Summer"
10  ->  "Fall"
12  ->  "Winter"

HINT:
- Use if/elif/else
- You can use 'in' to check: if month in [3, 4, 5]
- Or use ranges: if 3 <= month <= 5
"""


def get_season(month):
    """
    Return the season for the given month.

    Args:
        month: month number (1-12)
    Returns:
        "Spring", "Summer", "Fall", or "Winter"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing get_season()...")
    print("-" * 40)

    tests = [
        (1, "Winter"),
        (2, "Winter"),
        (3, "Spring"),
        (4, "Spring"),
        (5, "Spring"),
        (6, "Summer"),
        (7, "Summer"),
        (8, "Summer"),
        (9, "Fall"),
        (10, "Fall"),
        (11, "Fall"),
        (12, "Winter"),
    ]

    all_passed = True
    for i, (month, expected) in enumerate(tests, 1):
        result = get_season(month)
        if result == expected:
            print(f"Test {i}: PASSED  month {month} -> {result}")
        else:
            print(f"Test {i}: FAILED  month {month} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
