# https://leetcode.com/problems/single-number-ii/

from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = defaultdict(int)
        for n in nums:
            f[n] += 1
        for k, v in f.items():
            if v == 1:
                return k

        return -1


def test():
    s = Solution()
    assert s.singleNumber([2, 2, 3, 2]) == 3
    assert s.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
