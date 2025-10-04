# https://www.hackerrank.com/challenges/bit-manipulation-lonely-integer/problem
# HackerRank: Bit Manipulation - Lonely Integer
from functools import reduce
from operator import xor


def lonely_integer(arr: list[int]) -> int:
    """XOR all elements so the paired values cancel, leaving the unique one."""
    # Time: O(n)   Space: O(1)
    return reduce(xor, arr, 0)


def test() -> None:
    assert lonely_integer([1, 1, 2]) == 2
    assert lonely_integer([0, 0, 1, 2, 1]) == 2
    # edge case: single element
    assert lonely_integer([7]) == 7
