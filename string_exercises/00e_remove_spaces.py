"""
=== Exercise 0e: Remove All Spaces ===

TASK:
Remove all spaces from a string.

EXAMPLES:
"hello world"      ->  "helloworld"
"a b c d"          ->  "abcd"
"no spaces"        ->  "nospaces"
"   spaces   "     ->  "spaces"
""                 ->  ""

HINT:
- Loop through each character
- If the character is NOT a space, add it to the result
- Space character is " " or you can check: char != " "
"""


def remove_spaces(s):
    """
    Remove all spaces from the string.

    Args:
        s: a string
    Returns:
        The string with all spaces removed
    """
    # YOUR CODE HERE
    result = ""

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing remove_spaces()...")
    print("-" * 40)

    tests = [
        ("hello world", "helloworld"),
        ("a b c d", "abcd"),
        ("no spaces", "nospaces"),
        ("   spaces   ", "spaces"),
        ("", ""),
        ("nospace", "nospace"),
        ("   ", ""),
        ("a b", "ab"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = remove_spaces(input_str)
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
