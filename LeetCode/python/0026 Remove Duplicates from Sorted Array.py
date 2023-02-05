# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


def test():
    s = Solution()

    nums = [1, 1, 2]
    new_l = s.removeDuplicates(nums)
    assert new_l == 2
    assert nums[:new_l] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_l = s.removeDuplicates(nums)
    assert new_l == 5
    assert nums[:new_l] == [0, 1, 2, 3, 4]
