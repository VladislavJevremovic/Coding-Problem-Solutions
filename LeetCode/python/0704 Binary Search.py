# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Classic binary search: halve the [a, b] window each step until the
        target is found or the window is empty."""
        # Time: O(log n)   Space: O(1)
        a, b = 0, len(nums) - 1
        while a <= b:
            m = a + (b - a) // 2
            if nums[m] < target:
                a = m + 1
            elif nums[m] > target:
                b = m - 1
            else:
                return m

        return -1


def test():
    s = Solution()
    assert s.search([5], 5) == 0
    assert s.search([5], -5) == -1
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
