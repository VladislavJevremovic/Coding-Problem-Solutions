# https://leetcode.com/problems/largest-perimeter-triangle/

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0

        B = sorted(A)
        i = n - 3
        while i >= 0 and B[i] + B[i + 1] <= B[i + 2]:
            i -= 1

        return B[i] + B[i + 1] + B[i + 2] if i >= 0 else 0


def test():
    s = Solution()
    assert s.largestPerimeter([2, 1, 2]) == 5
    assert s.largestPerimeter([1, 2, 1]) == 0
    assert s.largestPerimeter([3, 2, 3, 4]) == 10
    assert s.largestPerimeter([3, 6, 2, 3]) == 8
