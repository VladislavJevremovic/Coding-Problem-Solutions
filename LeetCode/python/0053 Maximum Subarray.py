# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        current_maximum = nums[0]
        maximum = current_maximum

        for i in range(1, len(nums)):
            current_maximum = max(current_maximum + nums[i], nums[i])
            maximum = max(maximum, current_maximum)

        return maximum


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

    def maxSubArrayHelper(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]

        m = left + (right - left) // 2

        max_lsum = self.maxSubArrayHelper(nums, left, m)
        max_rsum = self.maxSubArrayHelper(nums, m + 1, right)
        max_xsum = self.maxSubArrayCrossing(nums, left, m, right)

        return max(max_lsum, max_rsum, max_xsum)

    def maxSubArrayCrossing(self, nums: List[int], left: int, mid: int, right: int) -> int:
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, left - 1, -1):
            sum += nums[i]
            if sum > left_sum:
                left_sum = sum

        right_sum = float('-inf')
        sum = 0
        for i in range(mid + 1, right + 1):
            sum += nums[i]
            if sum > right_sum:
                right_sum = sum

        return left_sum + right_sum


def test():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
