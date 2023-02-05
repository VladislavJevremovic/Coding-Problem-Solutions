# https://leetcode.com/problems/minimum-path-sum/

from typing import List


class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        infinity = float("inf")

        n = len(grid)  # h
        if not n:
            return 0
        m = len(grid[0])  # w
        if not m:
            return 0

        def dfs(grid, sums, x, y):
            if x + 1 > n or y + 1 > m:
                return infinity

            if x + 1 == n and y + 1 == m:
                return grid[x][y]

            if sums[x][y] != infinity:
                return sums[x][y]

            sums[x][y] = min(min(infinity, dfs(grid, sums, x + 1, y) + grid[x][y]),
                             dfs(grid, sums, x, y + 1) + grid[x][y])

            return sums[x][y]

        sums = [[infinity] * m for _ in range(n)]

        return dfs(grid, sums, 0, 0)


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # h
        if not m:
            return 0
        n = len(grid[0])  # w
        if not n:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]


def test():
    s = Solution2()
    assert s.minPathSum([[]]) == 0
    assert s.minPathSum([[1]]) == 1
    assert s.minPathSum([[1, 2]]) == 3
    assert s.minPathSum([[1], [2]]) == 3
    assert s.minPathSum([[1, 2], [3, 4]]) == 7
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum(
        [[9, 9, 0, 8, 9, 0, 5, 7, 2, 2, 7, 0, 8, 0, 2, 4, 8], [4, 4, 2, 7, 6, 0, 9, 7, 3, 2, 5, 4, 6, 5, 4, 8, 7],
         [4, 9, 7, 0, 7, 9, 2, 4, 0, 2, 4, 4, 6, 2, 8, 0, 7], [7, 7, 9, 6, 6, 4, 8, 4, 8, 7, 9, 4, 7, 6, 9, 6, 5],
         [1, 3, 7, 5, 7, 9, 7, 3, 3, 3, 8, 3, 6, 5, 0, 3, 6], [7, 1, 0, 7, 5, 0, 6, 6, 5, 3, 2, 6, 0, 0, 9, 5, 7],
         [6, 5, 6, 3, 8, 1, 8, 6, 4, 4, 3, 4, 9, 9, 3, 3, 1], [1, 0, 2, 9, 7, 9, 3, 1, 7, 5, 1, 8, 2, 8, 4, 7, 6],
         [9, 6, 7, 7, 4, 1, 4, 0, 6, 5, 1, 9, 0, 3, 2, 1, 7], [2, 0, 8, 7, 1, 7, 4, 3, 5, 6, 1, 9, 4, 0, 0, 2, 7],
         [9, 8, 1, 3, 8, 7, 1, 2, 8, 3, 7, 3, 4, 6, 7, 6, 6], [4, 8, 3, 8, 1, 0, 4, 4, 1, 0, 4, 1, 4, 4, 0, 3, 5],
         [6, 3, 4, 7, 5, 4, 2, 2, 7, 9, 8, 4, 5, 6, 0, 3, 9],
         [0, 4, 9, 7, 1, 0, 7, 7, 3, 2, 1, 4, 7, 6, 0, 0, 0]]) == 77
