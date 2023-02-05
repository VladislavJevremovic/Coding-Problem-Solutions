# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 0
        if not matrix or not matrix[0]:
            return result

        m, n = len(matrix), len(matrix[0])
        visited = {}

        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, i, j, visited)
                result = max(result, path)

        return result

    def dfs(self, matrix: List[List[int]], x: int, y: int, visited: dict) -> int:
        m, n = len(matrix), len(matrix[0])
        if (x, y) in visited:
            return visited.get((x, y))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        result = 1
        for d_x, d_y in directions:
            n_x = x + d_x
            n_y = y + d_y
            if 0 <= n_x < m and 0 <= n_y < n and matrix[n_x][n_y] > matrix[x][y]:
                result = max(result, self.dfs(matrix, n_x, n_y, visited) + 1)
        visited[(x, y)] = result

        return visited[(x, y)]


def test():
    s = Solution()
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
