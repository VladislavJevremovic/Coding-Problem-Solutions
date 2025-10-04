# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Painless

from functools import reduce
from operator import xor
from typing import List


def solution(A: List[int]) -> int:
    """XOR all elements so paired values cancel out, leaving the single unpaired value."""
    # Time: O(n)   Space: O(1)
    return reduce(xor, A)


def test() -> None:
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
    assert solution([42]) == 42
    assert solution([1, 2, 1]) == 2
