# https://leetcode.com/problems/rotting-oranges/

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        nr = len(grid)
        nc = len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        q = [(i, j) for i in range(nr) for j in range(nc) if grid[i][j] == 2]
        time = 0

        while True:
            new_q = []

            for _ in range(len(q)):
                (i, j) = q.pop()
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < nr and 0 <= nj < nc and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        new_q.append((ni, nj))

            q = new_q
            if not q:
                ok_left = any(1 in grid[i] for i in range(nr))
                return time if not ok_left else -1

            time += 1


def test():
    s = Solution()
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0
