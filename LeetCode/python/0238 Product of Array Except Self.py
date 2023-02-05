# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in reversed(range(n - 1)):
            result[i] = result[i + 1] * nums[i + 1]

        left = 1
        for i in range(n):
            result[i] = result[i] * left
            left *= nums[i]

        return result


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        result[0] = 1
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]

        right = 1
        for i in reversed(range(n)):
            result[i] = result[i] * right
            right *= nums[i]

        return result


def test():
    s = Solution1()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
