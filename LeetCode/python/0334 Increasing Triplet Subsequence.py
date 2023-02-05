# https://leetcode.com/problems/increasing-triplet-subsequence/

import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = second_num = math.inf
        for n in nums:
            if n <= first_num:  # is smallest?
                first_num = n
            elif n <= second_num:  # is second smallest?
                second_num = n
            else:  # n larger than both, found the triplet
                return True

        return False


def test():
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert s.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert s.increasingTriplet([2, 1, 5, 0, 4, 6]) is True
