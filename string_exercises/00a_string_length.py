"""
=== Exercise 0a: Count String Length (Without len()) ===

TASK:
Count how many characters are in a string WITHOUT using the len() function.
Use a loop to count each character one by one.

EXAMPLES:
"hello"  ->  5
"Python" ->  6
""       ->  0
"a b c"  ->  5  (spaces count too!)

HINT:
- Start with count = 0
- Use a for loop: for char in s:
- Add 1 to count for each character
"""


def string_length(s):
    """
    Count the number of characters in the string (without using len()).

    Args:
        s: a string
    Returns:
        The number of characters (int)
    """
    # YOUR CODE HERE
    # DO NOT use len()!
    count = 0

    return count


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing string_length()...")
    print("-" * 40)

    tests = [
        ("hello", 5),
        ("Python", 6),
        ("", 0),
        ("a b c", 5),
        ("12345", 5),
        ("!", 1),
        ("Hello World", 11),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = string_length(input_str)
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' has {result} characters")
        else:
            print(f"Test {i}: FAILED  '{input_str}' -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
