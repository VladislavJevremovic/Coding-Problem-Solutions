# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False

        x, y = m - 1, 0
        while 0 <= x and y <= n - 1:
            v = matrix[x][y]
            if v > target:
                x -= 1
            elif v < target:
                y += 1
            else:
                return True

        return False


def test():
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    assert s.searchMatrix(matrix, 5) is True
    assert s.searchMatrix(matrix, 20) is False
    assert s.searchMatrix([], 0) is False
