"""
=== Exercise 00b: Dice Roll Sum ===

TASK:
Given two dice values, calculate the sum and determine the result:
- Sum is 7 or 11: "win"
- Sum is 2, 3, or 12: "lose"
- Any other sum: "continue"

This is based on the game "Craps"!

EXAMPLES:
(3, 4)  ->  "win"      (sum = 7)
(6, 5)  ->  "win"      (sum = 11)
(1, 1)  ->  "lose"     (sum = 2)
(6, 6)  ->  "lose"     (sum = 12)
(2, 3)  ->  "continue" (sum = 5)

HINT:
- First calculate the sum
- Check if sum is in the winning numbers
- Check if sum is in the losing numbers
- Otherwise continue
"""


def dice_result(die1, die2):
    """
    Determine the result of a dice roll.

    Args:
        die1: value of first die (1-6)
        die2: value of second die (1-6)
    Returns:
        "win", "lose", or "continue"
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing dice_result()...")
    print("-" * 40)

    tests = [
        ((3, 4), "win"),      # 7
        ((6, 5), "win"),      # 11
        ((5, 6), "win"),      # 11
        ((1, 6), "win"),      # 7
        ((1, 1), "lose"),     # 2
        ((1, 2), "lose"),     # 3
        ((6, 6), "lose"),     # 12
        ((2, 3), "continue"), # 5
        ((4, 4), "continue"), # 8
        ((3, 3), "continue"), # 6
    ]

    all_passed = True
    for i, (dice, expected) in enumerate(tests, 1):
        d1, d2 = dice
        result = dice_result(d1, d2)
        total = d1 + d2
        if result == expected:
            print(f"Test {i}: PASSED  {d1}+{d2}={total} -> {result}")
        else:
            print(f"Test {i}: FAILED  {d1}+{d2}={total} -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
