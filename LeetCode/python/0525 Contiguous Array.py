# https://leetcode.com/problems/contiguous-array/

from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        indices[0] = [-1]
        c = 0
        for i, num in enumerate(nums):
            c += 1 if num == 1 else -1
            indices[c] += [i]

        return max([v[-1] - v[0] for v in indices.values()])


def test():
    s = Solution()
    assert s.findMaxLength([0, 1]) == 2
    assert s.findMaxLength([0, 1, 0]) == 2
    assert s.findMaxLength([0, 1, 0, 0, 0, 1]) == 2
