"""
=== Exercise 00c: Can Vote ===

TASK:
Check if a person is old enough to vote.
Voting age is 18 or older.

EXAMPLES:
18  ->  True
21  ->  True
17  ->  False
5   ->  False

HINT:
- Simple comparison: age >= 18
"""


def can_vote(age):
    """
    Check if someone with this age can vote.

    Args:
        age: the person's age
    Returns:
        True if can vote (18+), False otherwise
    """
    # YOUR CODE HERE
    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing can_vote()...")
    print("-" * 40)

    tests = [
        (18, True),
        (21, True),
        (17, False),
        (5, False),
        (100, True),
        (0, False),
        (19, True),
    ]

    all_passed = True
    for i, (age, expected) in enumerate(tests, 1):
        result = can_vote(age)
        status = "can vote" if result else "cannot vote"
        if result == expected:
            print(f"Test {i}: PASSED  age {age} -> {status}")
        else:
            print(f"Test {i}: FAILED  age {age} -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
