# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side_length = 0

        if not matrix:
            return max_side_length

        m = len(matrix)
        if not m:
            return max_side_length

        n = len(matrix[0])
        if not n:
            return max_side_length

        dp = [[0 for _ in range(n)] for _ in
              range(m)]  # dp[i][j] = maximum square side length up ending/with bottom-right at (i, j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':  # initialize smallest squares from given matrix
                    dp[i][j] = 1

                    if not max_side_length:
                        max_side_length = 1  # update maximum

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j]:  # transition: 1x1 square at (i, j) adds 1x1 to sum; if surrounded by 1's, that's 2x2
                    dp[i][j] = min(min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + 1

                    max_side_length = max(max_side_length, dp[i][j])  # update maximum

        return max_side_length ** 2  # return area


def test():
    s = Solution()
    assert s.maximalSquare(
        [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'],
         ['1', '0', '0', '1', '0']]) == 4
