# https://leetcode.com/problems/max-consecutive-ones/

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r, c = 0, 0
        for num in nums:
            if num > 0:
                c += 1
            else:
                c = 0

            r = max(r, c)

        return r


def test():
    s = Solution()
    assert s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert s.findMaxConsecutiveOnes([1]) == 1
    assert s.findMaxConsecutiveOnes([0]) == 0
    assert s.findMaxConsecutiveOnes([1, 1]) == 2
    assert s.findMaxConsecutiveOnes([0, 0]) == 0
    assert s.findMaxConsecutiveOnes([0, 1]) == 1
    assert s.findMaxConsecutiveOnes([1, 0]) == 1
