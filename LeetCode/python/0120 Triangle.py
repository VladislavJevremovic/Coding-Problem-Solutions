# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        result = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(len(triangle[i])):
                result[j] = min(result[j], result[j + 1]) + triangle[i][j]

        return result[0]


def test():
    s = Solution()
    assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert s.minimumTotal([[-10]]) == -10
