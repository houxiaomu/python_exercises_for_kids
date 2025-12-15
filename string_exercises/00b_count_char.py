"""
=== Exercise 0b: Count a Specific Character ===

TASK:
Count how many times a specific character appears in a string.
The search should be case-sensitive (uppercase and lowercase are different).

EXAMPLES:
count_char("hello", "l")     ->  2
count_char("Mississippi", "s") ->  4
count_char("Mississippi", "S") ->  0  (capital S not found)
count_char("aaa", "a")       ->  3
count_char("abc", "z")       ->  0

HINT:
- Loop through each character in the string
- If it matches the target character, add 1 to count
"""


def count_char(s, char):
    """
    Count how many times 'char' appears in string 's'.

    Args:
        s: a string to search in
        char: a single character to count
    Returns:
        The count (int)
    """
    # YOUR CODE HERE
    count = 0

    return count


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing count_char()...")
    print("-" * 40)

    tests = [
        (("hello", "l"), 2),
        (("Mississippi", "s"), 4),
        (("Mississippi", "S"), 0),
        (("aaa", "a"), 3),
        (("abc", "z"), 0),
        (("", "a"), 0),
        (("banana", "a"), 3),
        (("HELLO", "L"), 2),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        s, char = inputs
        result = count_char(s, char)
        if result == expected:
            print(f"Test {i}: PASSED  '{s}' has {result} '{char}'s")
        else:
            print(f"Test {i}: FAILED  count_char('{s}', '{char}') -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
