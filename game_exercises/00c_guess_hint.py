"""
=== Exercise 00c: Guess the Number - Hint ===

TASK:
In a number guessing game, give the player a hint!
Compare the guess to the secret number:
- If guess is correct: return "correct"
- If guess is too high: return "too high"
- If guess is too low: return "too low"

EXAMPLES:
secret=50, guess=50  ->  "correct"
secret=50, guess=75  ->  "too high"
secret=50, guess=25  ->  "too low"

HINT:
- Simple comparisons: ==, >, <
"""


def get_hint(secret, guess):
    """
    Give a hint for a number guessing game.

    Args:
        secret: the secret number to guess
        guess: the player's guess
    Returns:
        "correct", "too high", or "too low"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing get_hint()...")
    print("-" * 40)

    tests = [
        ((50, 50), "correct"),
        ((50, 75), "too high"),
        ((50, 25), "too low"),
        ((100, 100), "correct"),
        ((1, 5), "too high"),
        ((10, 3), "too low"),
        ((42, 42), "correct"),
    ]

    all_passed = True
    for i, (inputs, expected) in enumerate(tests, 1):
        secret, guess = inputs
        result = get_hint(secret, guess)
        if result == expected:
            print(f"Test {i}: PASSED  secret={secret}, guess={guess} -> {result}")
        else:
            print(f"Test {i}: FAILED  secret={secret}, guess={guess} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
