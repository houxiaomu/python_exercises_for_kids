"""
=== Exercise 5: Word Counter ===

TASK:
Write a function that counts how many times each word appears in a sentence.
Return a dictionary with words as keys and counts as values.
Words should be converted to lowercase.

EXAMPLES:
"hello world hello" -> {"hello": 2, "world": 1}
"The cat and the dog" -> {"the": 2, "cat": 1, "and": 1, "dog": 1}
"one fish two fish" -> {"one": 1, "fish": 2, "two": 1}

HINT:
- Use .split() to break the sentence into words
- Use .lower() to make all words lowercase
- Create an empty dictionary {}
- Loop through each word:
  - If word is already in dictionary, add 1 to its count
  - If word is not in dictionary, set its count to 1
"""


def count_words(sentence):
    """
    Count occurrences of each word in the sentence.

    Args:
        sentence: a string containing words
    Returns:
        A dictionary with word counts
    """
    # YOUR CODE HERE
    word_counts = {}

    return word_counts


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing count_words()...")
    print("-" * 40)

    tests = [
        ("hello world hello", {"hello": 2, "world": 1}),
        ("The cat and the dog", {"the": 2, "cat": 1, "and": 1, "dog": 1}),
        ("one fish two fish", {"one": 1, "fish": 2, "two": 1}),
        ("a a a b b c", {"a": 3, "b": 2, "c": 1}),
        ("Python", {"python": 1}),
        ("", {}),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = count_words(input_str)
        if result == expected:
            print(f"Test {i}: PASSED")
            print(f"   '{input_str}' -> {result}")
        else:
            print(f"Test {i}: FAILED")
            print(f"   Input: '{input_str}'")
            print(f"   Got: {result}")
            print(f"   Expected: {expected}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! You're a word counting wizard!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
