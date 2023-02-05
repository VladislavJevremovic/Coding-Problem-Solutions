# https://leetcode.com/problems/shuffle-an-array/

import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = self.original[:]

        return self.array

    def shuffle(self) -> List[int]:
        n = len(self.array)
        for i in range(n):
            swap_i = random.randrange(i, n)
            self.array[i], self.array[swap_i] = self.array[swap_i], self.array[i]

        return self.array


def test():
    nums = [1, 2, 3]
    s = Solution(nums)
    s.shuffle()
    assert s.reset() == [1, 2, 3]
