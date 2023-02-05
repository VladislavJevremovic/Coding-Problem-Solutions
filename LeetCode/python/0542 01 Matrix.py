# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            (x, y) = q.popleft()
            for (dx, dy) in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0 <= new_y < n and mat[new_x][new_y] < 0:
                    mat[new_x][new_y] = mat[x][y] + 1
                    q.append((new_x, new_y))

        return mat


def test():
    s = Solution()
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert s.updateMatrix([[0], [0], [0], [0], [0]]) == [[0], [0], [0], [0], [0]]
