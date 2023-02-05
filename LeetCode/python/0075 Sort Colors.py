# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        r = [0, 0, 0]
        for n in nums:
            r[n] += 1

        p = 0
        for i, c in enumerate(r):
            for _ in range(c):
                nums[p] = i
                p += 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        l1 = 0
        r1 = len(nums) - 1

        for num in nums:
            if num == 0:
                l1 += 1
            elif num == 2:
                r1 -= 1

        nums[:l1] = [0] * l1
        nums[l1:r1 + 1] = [1] * (r1 + 1 - l1)
        nums[r1 + 1:] = [2] * (len(nums) - r1 - 1)


def test():
    s = Solution2()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
