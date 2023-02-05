# https://leetcode.com/problems/jump-game

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True

        furthest_index = nums[0]  # how far can we reach
        for i, num in enumerate(nums):
            if furthest_index <= i and not num:
                return False  # can't progress past furthest_index (or i)

            furthest_index = max(furthest_index, i + num)
            if furthest_index >= n - 1:
                return True

        return False


def test():
    s = Solution()
    assert s.canJump([]) is True
    assert s.canJump([0]) is True
    assert s.canJump([1]) is True
    assert s.canJump([1, 2]) is True
    assert s.canJump([0, 2, 3]) is False
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
