"""
=== Exercise 01: Card Value (Blackjack) ===

TASK:
In Blackjack, each card has a value:
- Number cards (2-10): face value
- Face cards (J, Q, K): 10 points
- Ace (A): 11 points (simplified)

Given a card, return its point value.

EXAMPLES:
"2"  ->  2
"10" ->  10
"J"  ->  10
"Q"  ->  10
"K"  ->  10
"A"  ->  11

HINT:
- Check if it's a face card (J, Q, K)
- Check if it's an Ace
- Otherwise convert the string to a number
"""


def card_value(card):
    """
    Get the Blackjack value of a card.

    Args:
        card: a string like "2", "10", "J", "Q", "K", "A"
    Returns:
        The point value (integer)
    """
    # YOUR CODE HERE
    return 0


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing card_value()...")
    print("-" * 40)

    tests = [
        ("2", 2),
        ("5", 5),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
        ("A", 11),
        ("7", 7),
        ("9", 9),
    ]

    all_passed = True
    for i, (card, expected) in enumerate(tests, 1):
        result = card_value(card)
        if result == expected:
            print(f"Test {i}: PASSED  card '{card}' = {result} points")
        else:
            print(f"Test {i}: FAILED  card '{card}' -> {result} (expected {expected})")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
