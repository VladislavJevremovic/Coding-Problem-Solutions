# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        q = [(0, 0, 1)]
        grid[0][0] = 1
        while q:
            new_q = []
            for x, y, d in q:
                grid[x][y] = 1
                if (x, y) == (n - 1, n - 1):
                    return d

                grid[x][y] = 1
                for d_x, d_y in directions:
                    n_x, n_y = x + d_x, y + d_y
                    if 0 <= n_x < n and 0 <= n_y < n and not grid[n_x][n_y]:
                        new_q.append((n_x, n_y, d + 1))
                        grid[n_x][n_y] = 1
            q = new_q

        return -1


def test():
    s = Solution()
    assert s.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
