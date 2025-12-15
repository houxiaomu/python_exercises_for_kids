"""
=== Exercise 0d: Get First and Last Character ===

TASK:
Return a new string containing only the first and last character of the input.
If the string has only 1 character, return that character twice.
If the string is empty, return an empty string.

EXAMPLES:
"hello"   ->  "ho"
"Python"  ->  "Pn"
"a"       ->  "aa"
"ab"      ->  "ab"
""        ->  ""

HINT:
- First character: s[0]
- Last character: s[-1] or s[len(s)-1]
- Check the length first to handle special cases
"""


def first_and_last(s):
    """
    Return a string with only the first and last characters.

    Args:
        s: a string
    Returns:
        A new string with first and last characters
    """
    # YOUR CODE HERE

    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing first_and_last()...")
    print("-" * 40)

    tests = [
        ("hello", "ho"),
        ("Python", "Pn"),
        ("a", "aa"),
        ("ab", "ab"),
        ("", ""),
        ("coding", "cg"),
        ("12345", "15"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = first_and_last(input_str)
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' -> '{result}'")
        else:
            print(f"Test {i}: FAILED  '{input_str}' -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
