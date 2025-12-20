"""
=== Exercise 02: Tic-Tac-Toe Winner ===

TASK:
Check if there's a winner in Tic-Tac-Toe!
The board is a list of 9 cells (0-8):
 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8

Each cell contains "X", "O", or "" (empty).

Return:
- "X" if X wins
- "O" if O wins
- "tie" if board is full with no winner
- "ongoing" if game is not finished

Winning lines:
- Rows: [0,1,2], [3,4,5], [6,7,8]
- Columns: [0,3,6], [1,4,7], [2,5,8]
- Diagonals: [0,4,8], [2,4,6]

EXAMPLES:
["X","X","X","O","O","","","",""]  ->  "X"  (top row)
["X","O","X","O","O","O","X","",""]  ->  "O"  (middle row)
["X","O","X","O","X","O","O","X","O"] ->  "tie"

HINT:
- Check all 8 winning lines
- For each line, check if all 3 cells are the same (and not empty)
"""


def check_winner(board):
    """
    Check for a winner in Tic-Tac-Toe.

    Args:
        board: a list of 9 strings ("X", "O", or "")
    Returns:
        "X", "O", "tie", or "ongoing"
    """
    # YOUR CODE HERE
    # Define winning lines
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    return "ongoing"


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing check_winner()...")
    print("-" * 40)

    tests = [
        # X wins
        (["X","X","X","O","O","","","",""], "X"),  # top row
        (["X","O","","X","O","","X","",""], "X"),  # left column
        (["X","O","O","","X","","","","X"], "X"),  # diagonal
        # O wins
        (["X","X","","O","O","O","X","",""], "O"),  # middle row
        (["X","O","X","","O","","X","O",""], "O"),  # middle column
        # Tie
        (["X","O","X","O","X","O","O","X","O"], "tie"),
        (["X","O","X","X","O","O","O","X","X"], "tie"),
        # Ongoing
        (["X","O","","","","","","",""], "ongoing"),
        (["","","","","","","","",""], "ongoing"),
        (["X","O","X","O","","","","",""], "ongoing"),
    ]

    all_passed = True
    for i, (board, expected) in enumerate(tests, 1):
        result = check_winner(board)
        if result == expected:
            print(f"Test {i}: PASSED  -> {result}")
        else:
            print(f"Test {i}: FAILED  -> '{result}' (expected '{expected}')")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("ALL TESTS PASSED! Great job!")
    else:
        print("Some tests failed. Keep trying!")
    return all_passed


if __name__ == "__main__":
    run_tests()
