# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution(object):
    def findMin(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        left, right = 0, n - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


def test():
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
