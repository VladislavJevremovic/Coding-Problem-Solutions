# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        n = len(mat)
        for i in range(n):
            r += mat[i][i] + mat[n - i - 1][i]

        if n % 2:
            r -= mat[n // 2][n // 2]

        return r


def test():
    s = Solution()
    assert s.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert s.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
    assert s.diagonalSum([[5]]) == 5
