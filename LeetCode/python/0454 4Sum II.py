# https://leetcode.com/problems/4sum-ii/

from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        """Hash all A+B pair sums, then for each C+D pair count how many stored
        sums equal its negation."""
        # Time: O(n^2)   Space: O(n^2)
        r = 0
        m = defaultdict(int)
        for a in A:
            for b in B:
                m[a + b] += 1
        for c in C:
            for d in D:
                diff = -(c + d)
                if diff in m:
                    r += m[diff]

        return r


def test():
    s = Solution()
    assert s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert s.fourSumCount([0], [0], [0], [0]) == 1
