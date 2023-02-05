# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from math import floor, log10
from typing import List


class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])


class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if not (floor(log10(num)) + 1) % 2])


def test():
    s = Solution2()
    assert s.findNumbers([12, 345, 2, 6, 7896]) == 2
    assert s.findNumbers([555, 901, 482, 1771]) == 1
