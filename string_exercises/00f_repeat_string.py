"""
=== Exercise 0f: Repeat a String ===

TASK:
Repeat a string n times and return the result.
Do NOT use the * operator - use a loop!

EXAMPLES:
repeat_string("ab", 3)   ->  "ababab"
repeat_string("hi", 2)   ->  "hihi"
repeat_string("x", 5)    ->  "xxxxx"
repeat_string("hello", 1) -> "hello"
repeat_string("any", 0)  ->  ""

HINT:
- Start with an empty result string
- Use a loop that runs n times
- Each time, add the original string to result
"""


def repeat_string(s, n):
    """
    Repeat the string s exactly n times.

    Args:
        s: a string to repeat
        n: number of times to repeat (int)
    Returns:
        The repeated string
    """
    # YOUR CODE HERE
    # DO NOT use s * n!
    result = ""

    return result


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing repeat_string()...")
    print("-" * 40)

    tests = [
        (("ab", 3), "ababab"),
        (("hi", 2), "hihi"),
        (("x", 5), "xxxxx"),
        (("hello", 1), "hello"),
        (("any", 0), ""),
        (("", 5), ""),
        (("abc", 4), "abcabcabcabc"),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        s, n = inputs
        result = repeat_string(s, n)
        if result == expected:
            print(f"Test {i}: PASSED  repeat_string('{s}', {n}) -> '{result}'")
        else:
            print(f"Test {i}: FAILED  repeat_string('{s}', {n}) -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
