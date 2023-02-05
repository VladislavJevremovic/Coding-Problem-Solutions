# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        n = len(nums)
        begin, end = 0, n - 1
        while begin <= end:
            mid = begin + (end - begin) // 2
            if nums[mid] == target:
                if isFirst:  # lower bound
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    end = mid - 1  # search left
                else:  # upper bound
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    begin = mid + 1  # search right
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1


def test():
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert s.searchRange([], 0) == [-1, -1]
