# https://www.hackerrank.com/challenges/intro-to-tutorial-challenges/problem
# HackerRank: Intro to Tutorial Challenges
from typing import List


def intro_tutorial(v: int, arr: List[int]) -> int:
    """Binary search for v in a sorted array; return its index or -1."""
    # Time: O(log n)   Space: O(1)
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == v:
            return mid
        if arr[mid] < v:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def test() -> None:
    assert intro_tutorial(4, [1, 4, 5, 7, 9, 12]) == 1
    assert intro_tutorial(1, [1, 4, 5, 7, 9, 12]) == 0
    assert intro_tutorial(12, [1, 4, 5, 7, 9, 12]) == 5
    assert intro_tutorial(3, [1, 4, 5, 7, 9, 12]) == -1
