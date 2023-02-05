# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        r = [1, 1]
        for row in range(rowIndex - 1):
            t = []
            for i in range(len(r) - 1):
                t.append(r[i] + r[i + 1])
            r = [1] + t + [1]

        return r


def test():
    s = Solution()
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1, 1]
    assert s.getRow(2) == [1, 2, 1]
    assert s.getRow(3) == [1, 3, 3, 1]
    assert s.getRow(4) == [1, 4, 6, 4, 1]
