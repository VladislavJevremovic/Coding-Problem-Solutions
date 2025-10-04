# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Accumulate a prefix sum, appending the running total at each index."""
        # Time: O(n)   Space: O(n)
        r = []
        s = 0
        for num in nums:
            s += num
            r.append(s)

        return r


def test():
    s = Solution()
    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
