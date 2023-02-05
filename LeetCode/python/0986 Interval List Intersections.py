# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        r = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                r.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return r


def test():
    s = Solution()
    assert s.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert s.intervalIntersection([[1, 3], [5, 9]], []) == []
    assert s.intervalIntersection([], [[4, 8], [10, 12]]) == []
    assert s.intervalIntersection([[1, 7]], [[3, 10]]) == [[3, 7]]
