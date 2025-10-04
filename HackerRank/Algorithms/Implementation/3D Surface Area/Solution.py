# https://www.hackerrank.com/challenges/3d-surface-area/problem
# HackerRank: 3D Surface Area
from typing import List


def surface_area(grid: List[List[int]]) -> int:
    """Sum top/bottom faces plus each cell's height exceeding its four neighbors."""
    # Time: O(n)   Space: O(1)
    rows = len(grid)
    cols = len(grid[0])
    area = 0
    for i in range(rows):
        for j in range(cols):
            height = grid[i][j]
            if height == 0:
                continue
            # Top and bottom faces.
            area += 2
            # Four side faces: exposed height versus each neighbor (0 outside grid).
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                neighbor = grid[ni][nj] if 0 <= ni < rows and 0 <= nj < cols else 0
                area += max(0, height - neighbor)
    return area


def test() -> None:
    assert surface_area([[1]]) == 6
    assert surface_area([[1, 3, 4], [2, 2, 3], [1, 2, 4]]) == 60
