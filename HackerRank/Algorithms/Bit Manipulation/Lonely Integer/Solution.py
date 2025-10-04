# https://www.hackerrank.com/challenges/lonely-integer/problem
# HackerRank: Lonely Integer
from functools import reduce
from operator import xor
from typing import List


def lonely_integer(a: List[int]) -> int:
    """Return the single element that appears once; all others appear twice."""
    # Time: O(n)   Space: O(1)
    return reduce(xor, a, 0)


def test() -> None:
    assert lonely_integer([1, 1, 2]) == 2
    assert lonely_integer([0, 0, 1, 2, 1]) == 2
    assert lonely_integer([7]) == 7
    assert lonely_integer([4, 9, 95, 93, 57, 4, 57, 93, 9]) == 95
