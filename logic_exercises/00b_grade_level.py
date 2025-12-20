"""
=== Exercise 00b: Grade Level ===

TASK:
Convert a score (0-100) to a letter grade.
Grading scale:
- 90-100: "A"
- 80-89:  "B"
- 70-79:  "C"
- 60-69:  "D"
- 0-59:   "F"

EXAMPLES:
95  ->  "A"
85  ->  "B"
72  ->  "C"
65  ->  "D"
45  ->  "F"

HINT:
- Use if/elif/else
- Check from highest to lowest, or lowest to highest
- Be careful with the boundaries (90, 80, 70, 60)
"""


def get_grade(score):
    """
    Convert a score to a letter grade.

    Args:
        score: a number from 0 to 100
    Returns:
        A letter grade ("A", "B", "C", "D", or "F")
    """
    # YOUR CODE HERE
    return ""


# ============ TEST CODE (DO NOT MODIFY) ============
def run_tests():
    print("Testing get_grade()...")
    print("-" * 40)

    tests = [
        (100, "A"),
        (95, "A"),
        (90, "A"),
        (89, "B"),
        (85, "B"),
        (80, "B"),
        (79, "C"),
        (72, "C"),
        (70, "C"),
        (65, "D"),
        (60, "D"),
        (59, "F"),
        (45, "F"),
        (0, "F"),
    ]

    all_passed = True
    for i, (score, expected) in enumerate(tests, 1):
        result = get_grade(score)
        if result == expected:
            print(f"Test {i}: PASSED  score {score} = grade {result}")
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
