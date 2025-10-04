# https://www.hackerrank.com/challenges/simple-array-sum/problem
# HackerRank: Simple Array Sum
from typing import List


def simple_array_sum(ar: List[int]) -> int:
    """Return the sum of all elements."""
    # Time: O(n)   Space: O(1)
    return sum(ar)


def test() -> None:
    assert simple_array_sum([1, 2, 3, 4, 10, 11]) == 31
    assert simple_array_sum([]) == 0
    assert simple_array_sum([5]) == 5
