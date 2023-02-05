# https://leetcode.com/problems/delete-and-earn/

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            prev = curr = 0
            for num in nums:
                prev, curr = curr, max(prev + num, curr)

            return curr

        points = [0] * (max(nums) + 1)
        for num in nums:
            points[num] += num

        return rob(points)  # boils down to house robber: take every other sum-column


def test():
    s = Solution()
    assert s.deleteAndEarn([3, 4, 2]) == 6
    assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
