# https://leetcode.com/problems/number-of-good-pairs/

import collections
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # r = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             r += 1

        # return r

        return sum(v * (v - 1) // 2 for v in collections.Counter(nums).values())


def test():
    s = Solution()
    assert s.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert s.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert s.numIdenticalPairs([1, 2, 3]) == 0
