"""
=== Exercise 3: Check Palindrome ===

TASK:
Write a function that checks if a string is a palindrome.
A palindrome reads the same forwards and backwards.
Ignore spaces and case (uppercase/lowercase).

EXAMPLES:
"racecar"      ->  True
"hello"        ->  False
"A man a plan a canal Panama" -> True (ignore spaces and case)
"Was it a car or a cat I saw" -> True

HINT:
- First, remove all spaces from the string
- Convert to lowercase
- Compare the string with its reverse
- You can use your reverse_string function or [::-1]
"""


def is_palindrome(s):
    """
    Check if the string is a palindrome (ignoring spaces and case).

    Args:
        s: a string
    Returns:
        True if palindrome, False otherwise
    """
    # YOUR CODE HERE
    # Step 1: Remove spaces and convert to lowercase

    # Step 2: Check if it equals its reverse

    return False


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing is_palindrome()...")
    print("-" * 40)

    tests = [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("Was it a car or a cat I saw", True),
        ("level", True),
        ("python", False),
        ("", True),
        ("a", True),
        ("Madam", True),
        ("No lemon no melon", True),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = is_palindrome(input_str)
        status = "PASSED" if result == expected else "FAILED"
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' -> {result}")
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
