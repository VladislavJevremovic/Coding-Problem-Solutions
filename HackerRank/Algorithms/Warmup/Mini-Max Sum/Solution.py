# https://www.hackerrank.com/challenges/mini-max-sum/problem
# HackerRank: Mini-Max Sum
from typing import List, Tuple


def mini_max_sum(arr: List[int]) -> Tuple[int, int]:
    """Return (min, max) sums obtainable by summing all but one element."""
    # Time: O(n)   Space: O(1)
    total = sum(arr)
    return total - max(arr), total - min(arr)


def test() -> None:
    assert mini_max_sum([1, 2, 3, 4, 5]) == (10, 14)
    assert mini_max_sum([7, 69, 2, 221, 8974]) == (299, 9271)
