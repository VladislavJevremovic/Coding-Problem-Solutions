# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        iteratingIndex = 0
        nextNonZeroPlacementIndex = 0
        while iteratingIndex < len(nums):
            if nums[iteratingIndex]:
                nums[nextNonZeroPlacementIndex], nums[iteratingIndex] = nums[iteratingIndex], nums[
                    nextNonZeroPlacementIndex]
                nextNonZeroPlacementIndex += 1

            iteratingIndex += 1


def test():
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
