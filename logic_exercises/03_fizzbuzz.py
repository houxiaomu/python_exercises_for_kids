"""
=== Exercise 03: FizzBuzz ===

TASK:
This is a famous programming challenge!
Given a number n, return:
- "FizzBuzz" if divisible by BOTH 3 and 5
- "Fizz" if divisible by 3 only
- "Buzz" if divisible by 5 only
- The number as a string if neither

EXAMPLES:
15  ->  "FizzBuzz"  (divisible by 3 and 5)
9   ->  "Fizz"      (divisible by 3 only)
10  ->  "Buzz"      (divisible by 5 only)
7   ->  "7"         (neither)

HINT:
- Check "FizzBuzz" FIRST (both 3 and 5)
- Then check Fizz (3 only)
- Then check Buzz (5 only)
- Otherwise return str(n)
"""


def fizzbuzz(n):
    """
    Return the FizzBuzz result for n.

    Args:
        n: a positive integer
    Returns:
        "FizzBuzz", "Fizz", "Buzz", or the number as a string
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing fizzbuzz()...")
    print("-" * 40)

    tests = [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (4, "4"),
        (5, "Buzz"),
        (6, "Fizz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (7, "7"),
    ]

    all_passed = True
    for i, (num, expected) in enumerate(tests, 1):
        result = fizzbuzz(num)
        if result == expected:
            print(f"Test {i}: PASSED  fizzbuzz({num}) = {result}")
        else:
            print(f"Test {i}: FAILED  fizzbuzz({num}) -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
