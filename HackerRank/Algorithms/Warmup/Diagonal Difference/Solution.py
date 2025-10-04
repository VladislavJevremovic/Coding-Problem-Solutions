# https://www.hackerrank.com/challenges/diagonal-difference/problem
# HackerRank: Diagonal Difference
from typing import List


def diagonal_difference(arr: List[List[int]]) -> int:
    """Absolute difference between the sums of the two diagonals of a square matrix."""
    # Time: O(n)   Space: O(1)
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


def test() -> None:
    assert diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15
    assert diagonal_difference([[1, 2], [3, 4]]) == 0
    assert diagonal_difference([[5]]) == 0
