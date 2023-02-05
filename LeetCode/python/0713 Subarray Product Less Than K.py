# https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List


class Solution:
    # invariant: left is smallest value (for each right) so the product in prod = nums[left] * ... * nums[right] < k
    # monotone increasing -> sliding
    # number of intervals: right = right - left + 1

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        result = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]  # move window right
                left += 1
            result += right - left + 1  # all shorter are OK, too

        return result


def test():
    s = Solution()
    assert s.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert s.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
