# https://www.hackerrank.com/challenges/angry-professor/problem
# HackerRank: Angry Professor
from typing import List


def angry_professor(k: int, a: List[int]) -> str:
    """Cancel class when fewer than k students arrive on time (arrival <= 0)."""
    # Time: O(n)   Space: O(1)
    on_time = sum(1 for arrival in a if arrival <= 0)
    return "YES" if on_time < k else "NO"


def test() -> None:
    assert angry_professor(3, [-1, -3, 4, 2]) == "YES"
    assert angry_professor(2, [0, -1, 2, 1]) == "NO"
