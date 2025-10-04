# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Subtract the actual sum from the expected 0..n sum (Gauss formula);
        the difference is the missing value."""
        # Time: O(n)   Space: O(1)
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


def test():
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
