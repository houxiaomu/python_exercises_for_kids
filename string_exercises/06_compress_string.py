"""
=== Exercise 6: String Compression (Challenge!) ===

TASK:
Compress a string by counting consecutive repeated characters.
Each character is followed by its count.

EXAMPLES:
"aaa"       ->  "a3"
"aaabbc"    ->  "a3b2c1"
"abcd"      ->  "a1b1c1d1"
"aaAAaa"    ->  "a2A2a2"  (case sensitive!)
"xxxyyyzz"  ->  "x3y3z2"

HINT:
- Keep track of the current character and its count
- When the next character is different, add current char + count to result
- Don't forget the last group of characters!
- Handle empty string specially
"""


def compress_string(s):
    """
    Compress the string using run-length encoding.

    Args:
        s: a string to compress
    Returns:
        The compressed string
    """
    # YOUR CODE HERE
    if len(s) == 0:
        return ""

    result = ""
    current_char = s[0]
    count = 1

    # Loop through the rest of the string (starting from index 1)

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing compress_string()...")
    print("-" * 40)

    tests = [
        ("aaa", "a3"),
        ("aaabbc", "a3b2c1"),
        ("abcd", "a1b1c1d1"),
        ("aaAAaa", "a2A2a2"),
        ("xxxyyyzz", "x3y3z2"),
        ("a", "a1"),
        ("", ""),
        ("aabbccdd", "a2b2c2d2"),
        ("aaaaaaaaaa", "a10"),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(tests, 1):
        result = compress_string(input_str)
        if result == expected:
            print(f"Test {i}: PASSED  '{input_str}' -> '{result}'")
        else:
            print(f"Test {i}: FAILED  '{input_str}' -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! You're a compression champion!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
