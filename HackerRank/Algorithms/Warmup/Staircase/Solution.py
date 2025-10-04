# https://www.hackerrank.com/challenges/staircase/problem
# HackerRank: Staircase
from typing import List


def staircase(n: int) -> List[str]:
    """Return the rows of a right-aligned staircase of height n made of '#'."""
    # Time: O(n^2)   Space: O(n^2)
    return [" " * (n - i) + "#" * i for i in range(1, n + 1)]


def test() -> None:
    assert staircase(4) == ["   #", "  ##", " ###", "####"]
    assert staircase(1) == ["#"]
    assert staircase(2) == [" #", "##"]
