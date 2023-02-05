# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            m = left + (right - left) // 2
            if nums[m] > nums[m + 1]:
                right = m
            else:
                left = m + 1

        return left


def test():
    s = Solution()
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
