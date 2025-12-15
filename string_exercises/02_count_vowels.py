"""
=== Exercise 2: Count Vowels ===

TASK:
Write a function that counts the number of vowels in a string.
Vowels are: a, e, i, o, u (both uppercase and lowercase count)

EXAMPLES:
"hello"      ->  2  (e, o)
"PYTHON"     ->  1  (O)
"aeiou"      ->  5
"bcdfg"      ->  0
"Beautiful"  ->  5  (e, a, u, i, u)

HINT:
- Create a string or list of vowels: "aeiou"
- Loop through each character in the input string
- Check if the character (converted to lowercase) is in the vowels
- Use .lower() to convert to lowercase
"""


def count_vowels(s):
    """
    Count the number of vowels in the string.

    Args:
        s: a string
    Returns:
        The count of vowels (int)
    """
    # YOUR CODE HERE
    count = 0

    return count


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing count_vowels()...")
    print("-" * 40)

    tests = [
        ("hello", 2),
        ("PYTHON", 1),
        ("aeiou", 5),
        ("AEIOU", 5),
        ("bcdfg", 0),
        ("Beautiful", 5),
        ("", 0),
        ("rhythm", 0),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = count_vowels(input_str)
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' -> {result} vowels")
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
