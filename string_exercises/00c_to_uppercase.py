"""
=== Exercise 0c: Convert to Uppercase ===

TASK:
Convert all lowercase letters in a string to uppercase.
Do NOT use the built-in .upper() method - do it yourself!

EXAMPLES:
"hello"   ->  "HELLO"
"Python"  ->  "PYTHON"
"ABC"     ->  "ABC"  (already uppercase)
"a1b2c3"  ->  "A1B2C3"  (numbers stay the same)

HINT:
- Lowercase letters are 'a' to 'z'
- You can check: if 'a' <= char <= 'z'
- To convert: use ord() to get ASCII code, subtract 32, use chr() to convert back
- Or use a simple lookup: create two strings "abcdefghijklmnopqrstuvwxyz" and "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""


def to_uppercase(s):
    """
    Convert all lowercase letters to uppercase (without using .upper()).

    Args:
        s: a string
    Returns:
        The string with all letters in uppercase
    """
    # YOUR CODE HERE
    # DO NOT use .upper()!
    result = ""

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing to_uppercase()...")
    print("-" * 40)

    tests = [
        ("hello", "HELLO"),
        ("Python", "PYTHON"),
        ("ABC", "ABC"),
        ("a1b2c3", "A1B2C3"),
        ("", ""),
        ("hello world", "HELLO WORLD"),
        ("123", "123"),
        ("MiXeD", "MIXED"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = to_uppercase(input_str)
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
