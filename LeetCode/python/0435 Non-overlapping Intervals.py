# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')  # previous interval end
        erased = 0
        for i in sorted(intervals, key=lambda i: i[1]):  # sort by interval end, ascending
            if i[0] >= end:
                end = i[1]  # keep one with earliest end, leaves most room for others
            else:
                erased += 1  # remove overlapping

        return erased


def test():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
