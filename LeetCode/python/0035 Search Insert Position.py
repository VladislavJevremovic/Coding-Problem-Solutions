# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        while a <= b:
            m = a + (b - a) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                b = m - 1
            else:
                a = m + 1

        return a


def test():
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([1], 0) == 0
