# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a = 0
        b = len(nums) - 1
        while a < b:
            m = a + (b - a) // 2
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    a = m + 2
                else:
                    b = m
            else:
                if nums[m] == nums[m - 1]:
                    a = m + 1
                else:
                    b = m - 1

        return nums[a]


def test():
    s = Solution()
    assert s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
