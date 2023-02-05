# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        r = 1
        for i in range(1, n):
            m = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, dp[j])

            dp[i] = m + 1
            r = max(r, dp[i])

        return r


def test():
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
