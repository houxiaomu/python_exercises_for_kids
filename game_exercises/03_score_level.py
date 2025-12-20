"""
=== Exercise 03: Game Score Level ===

TASK:
In a video game, players earn ranks based on their score:
- 0-999 points: "Bronze"
- 1000-4999 points: "Silver"
- 5000-9999 points: "Gold"
- 10000-19999 points: "Platinum"
- 20000+ points: "Diamond"

EXAMPLES:
500    ->  "Bronze"
2500   ->  "Silver"
7500   ->  "Gold"
15000  ->  "Platinum"
25000  ->  "Diamond"

HINT:
- Use if/elif/else
- Check from highest to lowest, or lowest to highest
"""


def get_rank(score):
    """
    Get the player's rank based on their score.

    Args:
        score: the player's score (non-negative integer)
    Returns:
        "Bronze", "Silver", "Gold", "Platinum", or "Diamond"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing get_rank()...")
    print("-" * 40)

    tests = [
        (0, "Bronze"),
        (500, "Bronze"),
        (999, "Bronze"),
        (1000, "Silver"),
        (2500, "Silver"),
        (4999, "Silver"),
        (5000, "Gold"),
        (7500, "Gold"),
        (9999, "Gold"),
        (10000, "Platinum"),
        (15000, "Platinum"),
        (19999, "Platinum"),
        (20000, "Diamond"),
        (50000, "Diamond"),
    ]

    all_passed = True
    for i, (score, expected) in enumerate(tests, 1):
        result = get_rank(score)
        if result == expected:
            print(f"Test {i}: PASSED  score {score} = {result}")
        else:
            print(f"Test {i}: FAILED  score {score} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
