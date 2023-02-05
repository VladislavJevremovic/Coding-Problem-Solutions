# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0] * n

        a = 0
        b = n - 1
        p = b
        while a <= b:
            a_s = nums[a] * nums[a]
            b_s = nums[b] * nums[b]
            if a_s > b_s:
                r[p] = a_s
                a += 1
            else:
                r[p] = b_s
                b -= 1

            p -= 1

        return r


def test():
    s = Solution()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
