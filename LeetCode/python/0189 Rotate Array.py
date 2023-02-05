# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or not k:
            return

        n = len(nums)
        k = k % n

        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums: List[int], i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        if not nums or n < 2:
            return

        k = k % n
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)


def test():
    s = Solution2()

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    s.rotate(nums, 2)
    assert nums == [3, 99, -1, -100]

    nums = [1]
    s.rotate(nums, 1)
    assert nums == [1]
