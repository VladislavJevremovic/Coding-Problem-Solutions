# https://leetcode.com/problems/arithmetic-slices/

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """DP: dp[i] = arithmetic slices ending at i; extend the previous run
        when the difference matches, summing all dp values."""
        # Time: O(n)   Space: O(n)
        n = len(nums)
        dp = [0] * n
        sum = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]
                sum += dp[i]

        return sum


def test():
    s = Solution()
    assert s.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert s.numberOfArithmeticSlices([1]) == 0
