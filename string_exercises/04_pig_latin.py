"""
=== Exercise 4: Pig Latin Converter ===

TASK:
Convert a word to Pig Latin using these rules:
1. If the word starts with a vowel (a, e, i, o, u), add "way" to the end
   Example: "apple" -> "appleway"
2. If the word starts with a consonant, move the first letter to the end
   and add "ay"
   Example: "hello" -> "ellohay"

EXAMPLES:
"apple"   ->  "appleway"
"hello"   ->  "ellohay"
"python"  ->  "ythonpay"
"ice"     ->  "iceway"
"smile"   ->  "milesay"

HINT:
- Check if the first character is a vowel
- Use string slicing: s[0] gets first char, s[1:] gets rest of string
- Use .lower() to check the first letter
"""


def to_pig_latin(word):
    """
    Convert a single word to Pig Latin.

    Args:
        word: a single word (string)
    Returns:
        The word in Pig Latin
    """
    # YOUR CODE HERE
    vowels = "aeiouAEIOU"

    # Check if word is empty
    if len(word) == 0:
        return ""

    # Check if first letter is a vowel

    return word


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing to_pig_latin()...")
    print("-" * 40)

    tests = [
        ("apple", "appleway"),
        ("hello", "ellohay"),
        ("python", "ythonpay"),
        ("ice", "iceway"),
        ("smile", "milesay"),
        ("egg", "eggway"),
        ("code", "odecay"),
        ("a", "away"),
        ("b", "bay"),
        ("elephant", "elephantway"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = to_pig_latin(input_str)
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' -> '{result}'")
        else:
            print(f"Test {i}: FAILED  '{input_str}' -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Ouyay areway amazingway!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
