# https://www.hackerrank.com/challenges/arrays-ds/problem
# HackerRank: Arrays - DS
from typing import List


def reverse_array(a: List[int]) -> List[int]:
    """Return the array reversed via slicing."""
    # Time: O(n)   Space: O(n)
    return a[::-1]


def test() -> None:
    assert reverse_array([1, 4, 3, 2]) == [2, 3, 4, 1]
    assert reverse_array([]) == []
    assert reverse_array([7]) == [7]
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
