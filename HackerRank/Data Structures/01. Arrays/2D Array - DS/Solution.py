# https://www.hackerrank.com/challenges/2d-array-ds/problem
# HackerRank: 2D Array - DS
from typing import List


def hourglass_sum(a: List[List[int]]) -> int:
    """Scan all 16 fixed 3x3 hourglass windows in the 6x6 grid, tracking the max sum."""
    # Time: O(1)   Space: O(1)  (grid is fixed 6x6 -> constant work)
    max_sum = float("-inf")
    for i in range(4):
        for j in range(4):
            total = (
                a[i][j]
                + a[i][j + 1]
                + a[i][j + 2]
                + a[i + 1][j + 1]
                + a[i + 2][j]
                + a[i + 2][j + 1]
                + a[i + 2][j + 2]
            )
            if total > max_sum:
                max_sum = total
    return int(max_sum)


def test() -> None:
    grid = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    # Best hourglass is centered at (3,3): 2+4+4 / 2 / 1+2+4 = 19
    assert hourglass_sum(grid) == 19

    all_neg = [[-1] * 6 for _ in range(6)]
    # Each hourglass has 7 cells of -1 -> -7
    assert hourglass_sum(all_neg) == -7
