"""
=== Exercise 1: Reverse a String ===

TASK:
Write a function that reverses a string.

EXAMPLES:
"hello"  ->  "olleh"
"Python" ->  "nohtyP"
"12345"  ->  "54321"

HINT:
- Method 1: Use a loop to build the reversed string
- Method 2: Use string slicing [::-1]
- Try both methods to learn!
"""


def reverse_string(s):
    """
    Reverse the given string.

    Args:
        s: a string to reverse
    Returns:
        The reversed string
    """
    # YOUR CODE HERE
    result = ""

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing reverse_string()...")
    print("-" * 40)

    tests = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("a", "a"),
        ("", ""),
        ("racecar", "racecar"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = reverse_string(input_str)
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
