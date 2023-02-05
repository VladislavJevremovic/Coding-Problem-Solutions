# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # pos, neg: length of pos/neg products ending at x
        r = pos = neg = 0
        for x in nums:
            if x > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0  # reset
            r = max(r, pos)

        return r


def test():
    s = Solution()
    assert s.getMaxLen([1, -2, -3, 4]) == 4
    assert s.getMaxLen([0, 1, -2, -3, -4]) == 3
    assert s.getMaxLen([-1, -2, -3, 0, 1]) == 2
    assert s.getMaxLen([-1, 2]) == 1
    assert s.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]) == 4
