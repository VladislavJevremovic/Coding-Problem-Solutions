# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > 1]


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return sorted(Solution().findDuplicates(list1)) == sorted(expected)

    assert case([4, 3, 2, 7, 8, 2, 3, 1], [2, 3])
    assert case([1, 1, 2], [1])
    assert case([1], [])
