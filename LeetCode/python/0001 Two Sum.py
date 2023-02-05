# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}  # number: index of complement
        for i, num in enumerate(nums):
            c = target - num  # complement of num at i
            if c in m:
                return [m[c], i]  # index in m was added earlier, hence first in result
            m[num] = i


def test():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
