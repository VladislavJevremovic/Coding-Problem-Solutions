# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHelper(nums: List[int]) -> int:
            t2, t1 = 0, 0
            for num in nums:
                t2, t1 = t1, max(t1, num + t2)

            return t1

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(robHelper(nums[:-1]), robHelper(nums[1:]))


def test():
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
    assert s.rob([1]) == 1
