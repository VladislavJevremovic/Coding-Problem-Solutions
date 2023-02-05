# https://leetcode.com/problems/minimum-size-subarray-sum/

import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = math.inf
        left = sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= target:
                result = min(result, i + 1 - left)  # if new subarray shorter?

                sum -= nums[left]  # move window right
                left += 1

        return result if result != math.inf else 0


def test():
    s = Solution()
    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
