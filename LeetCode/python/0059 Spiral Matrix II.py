# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        r = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        d = 'right'

        for i in range(1, n ** 2 + 1):
            r[x][y] = i
            if d == 'right':
                y += 1
                if y == n or r[x][y] > 0:
                    d = 'down'
                    y -= 1
                    x += 1
            elif d == 'down':
                x += 1
                if x == n or r[x][y] > 0:
                    d = 'left'
                    x -= 1
                    y -= 1
            elif d == 'left':
                y -= 1
                if y == -1 or r[x][y] > 0:
                    d = 'up'
                    y += 1
                    x -= 1
            elif d == 'up':
                x -= 1
                if y == -1 or r[x][y] > 0:
                    d = 'right'
                    x += 1
                    y += 1

        return r


def test():
    s = Solution()
    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(1) == [[1]]
