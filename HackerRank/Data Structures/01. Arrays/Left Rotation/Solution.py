# https://www.hackerrank.com/challenges/left-rotation/problem
# HackerRank: Left Rotation
from typing import List


def rotate_left(a: List[int], d: int) -> List[int]:
    """Rotate left by d via modulo split-and-concatenate of two slices."""
    # Time: O(n)   Space: O(n)
    if not a:
        return []
    d %= len(a)
    return a[d:] + a[:d]


def test() -> None:
    assert rotate_left([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
    assert rotate_left([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate_left([1, 2, 3], 1) == [2, 3, 1]
