# https://leetcode.com/problems/house-robber/

from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        """DP with two rolling variables: at each house choose the better of
        skipping it or robbing it plus the best two houses back."""
        # Time: O(n)   Space: O(1)
        prev, curr = 0, 0  # [-2], [-1]
        for num in nums:
            t = curr
            curr = max(prev + num, curr)
            prev = t

        return curr


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """Tabulated DP: dp[i] is the best loot using the first i houses, padded
        by two leading zeros to avoid edge cases."""
        # Time: O(n)   Space: O(n)
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(2, n + 2):
            dp[i] = max(dp[i - 1], nums[i - 2] + dp[i - 2])

        return dp[-1]


def test():
    s = Solution1()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
