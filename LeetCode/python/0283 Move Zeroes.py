# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Two pointers: scan with one index and swap each non-zero into the next
        free front slot, leaving the zeros pushed to the end in place."""
        # Time: O(n)   Space: O(1)
        iteratingIndex = 0
        nextNonZeroPlacementIndex = 0
        while iteratingIndex < len(nums):
            if nums[iteratingIndex]:
                nums[nextNonZeroPlacementIndex], nums[iteratingIndex] = (
                    nums[iteratingIndex],
                    nums[nextNonZeroPlacementIndex],
                )
                nextNonZeroPlacementIndex += 1

            iteratingIndex += 1


def test():
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
