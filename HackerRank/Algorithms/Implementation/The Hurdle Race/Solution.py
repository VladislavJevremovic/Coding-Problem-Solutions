# https://www.hackerrank.com/challenges/the-hurdle-race/problem
# HackerRank: The Hurdle Race
from typing import List


def hurdle_race(k: int, height: List[int]) -> int:
    """Doses needed equal the tallest hurdle minus jump height k, floored at 0."""
    # Time: O(n)   Space: O(1)
    return max(0, max(height) - k)


def test() -> None:
    assert hurdle_race(1, [1, 6, 3, 5, 2]) == 5
    assert hurdle_race(7, [2, 5, 4, 5, 2]) == 0
