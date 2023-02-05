# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

from typing import List


class BinaryMatrix(object):
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self) -> List[int]:
        return [len(self.matrix), len(self.matrix[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        m, n = binaryMatrix.dimensions()

        x, y, r = 0, n - 1, -1
        while y >= 0 and x <= m - 1:
            v = binaryMatrix.get(x, y)
            if v == 0:
                x += 1
            else:
                r = y
                y -= 1

        return r


def test():
    def case(matrix: List[List[int]], expected: int) -> bool:
        return Solution().leftMostColumnWithOne(BinaryMatrix(matrix)) == expected

    assert case([[0, 0], [1, 1]], 0)
    assert case([[0, 0], [0, 1]], 1)
    assert case([[0, 0], [0, 0]], -1)
    assert case([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]], 1)
