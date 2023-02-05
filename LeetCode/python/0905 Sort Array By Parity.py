# https://leetcode.com/problems/sort-array-by-parity

from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]


def test():
    s = Solution()
    assert s.sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1]
    assert s.sortArrayByParity([0]) == [0]
