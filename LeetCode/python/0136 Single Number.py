# https://leetcode.com/problems/single-number/

from functools import reduce
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR all values via reduce; duplicates cancel, leaving the unique
        number."""
        # Time: O(n)   Space: O(1)
        return reduce(lambda x, y: x ^ y, nums)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR-accumulate every value in a loop; pairs cancel out, leaving the
        unique number."""
        # Time: O(n)   Space: O(1)
        r = 0
        for num in nums:
            r ^= num

        return r


def test():
    s = Solution1()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
