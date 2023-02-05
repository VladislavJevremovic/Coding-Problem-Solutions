# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertion_index = 0
        iterating_index = 0
        while iterating_index < len(nums):
            if nums[iterating_index] != val:
                nums[insertion_index] = nums[iterating_index]
                insertion_index += 1
            iterating_index += 1

        return insertion_index


def test():
    s = Solution()
    assert s.removeElement([], 3) == 0
    assert s.removeElement([3], 3) == 0
    assert s.removeElement([3, 3], 3) == 0
    assert s.removeElement([3, 1, 3], 3) == 1
    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
