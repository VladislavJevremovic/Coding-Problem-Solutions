# https://www.hackerrank.com/challenges/grading/problem
# HackerRank: Grading Students
from typing import List


def grading_students(grades: List[int]) -> List[int]:
    """Round each grade up to the next multiple of 5 when within 3 of it."""

    # Time: O(n)   Space: O(n)
    def round_grade(g: int) -> int:
        if g < 38:
            return g
        next_multiple = ((g // 5) + 1) * 5
        return next_multiple if next_multiple - g < 3 else g

    return [round_grade(g) for g in grades]


def test() -> None:
    assert grading_students([73, 67, 38, 33]) == [75, 67, 40, 33]
    assert grading_students([84, 29, 57]) == [85, 29, 57]
