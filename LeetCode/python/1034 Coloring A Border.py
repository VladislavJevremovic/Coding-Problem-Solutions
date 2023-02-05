# https://leetcode.com/problems/coloring-a-border/

from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(grid: List[List[int]], i: int, j: int, targetColor: int, border: List[int],
                visited: List[List[bool]]) -> None:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] != targetColor:
                return

            visited[i][j] = True
            if isBorder(grid, i, j, targetColor):
                border.append([i, j])

            dfs(grid, i - 1, j, targetColor, border, visited)
            dfs(grid, i + 1, j, targetColor, border, visited)
            dfs(grid, i, j - 1, targetColor, border, visited)
            dfs(grid, i, j + 1, targetColor, border, visited)

        def isBorder(grid: List[List[int]], i: int, j: int, targetColor: int) -> bool:
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                return True

            return grid[i - 1][j] != targetColor or grid[i + 1][j] != targetColor or grid[i][j - 1] != targetColor or \
                   grid[i][j + 1] != targetColor

        border = []  # list of 2-item lists
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dfs(grid, r0, c0, grid[r0][c0], border, visited)
        for point in border:
            grid[point[0]][point[1]] = color

        return grid


def test():
    s = Solution()
    assert s.colorBorder([[1, 1], [1, 2]], 0, 0, 3) == [[3, 3], [3, 2]]
    assert s.colorBorder([[1, 2, 2], [2, 3, 2]], 0, 1, 3) == [[1, 3, 3], [2, 3, 3]]
    assert s.colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2) == [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
