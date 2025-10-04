# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# HackerRank: A Very Big Sum
from typing import List


def a_very_big_sum(ar: List[int]) -> int:
    """Return the sum of all elements (Python ints have no overflow)."""
    # Time: O(n)   Space: O(1)
    return sum(ar)


def test() -> None:
    assert (
        a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
        == 5000000015
    )
    assert a_very_big_sum([]) == 0
    assert a_very_big_sum([7]) == 7
