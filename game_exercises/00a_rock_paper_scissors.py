"""
=== Exercise 00a: Rock Paper Scissors ===

TASK:
Determine the winner of Rock-Paper-Scissors!
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choice = tie

Return:
- "player1" if player1 wins
- "player2" if player2 wins
- "tie" if same choice

EXAMPLES:
("rock", "scissors")  ->  "player1"  (rock beats scissors)
("paper", "rock")     ->  "player1"  (paper beats rock)
("scissors", "rock")  ->  "player2"  (rock beats scissors)
("rock", "rock")      ->  "tie"

HINT:
- First check for tie (same choice)
- Then check the 3 winning cases for player1
- Otherwise player2 wins
"""


def rock_paper_scissors(player1, player2):
    """
    Determine the winner of rock-paper-scissors.

    Args:
        player1: "rock", "paper", or "scissors"
        player2: "rock", "paper", or "scissors"
    Returns:
        "player1", "player2", or "tie"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing rock_paper_scissors()...")
    print("-" * 40)

    tests = [
        (("rock", "scissors"), "player1"),
        (("rock", "paper"), "player2"),
        (("rock", "rock"), "tie"),
        (("paper", "rock"), "player1"),
        (("paper", "scissors"), "player2"),
        (("paper", "paper"), "tie"),
        (("scissors", "paper"), "player1"),
        (("scissors", "rock"), "player2"),
        (("scissors", "scissors"), "tie"),
    ]

    all_passed = True
    for i, (moves, expected) in enumerate(tests, 1):
        p1, p2 = moves
        result = rock_paper_scissors(p1, p2)
        if result == expected:
            print(f"Test {i}: PASSED  {p1} vs {p2} -> {result}")
        else:
            print(f"Test {i}: FAILED  {p1} vs {p2} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
