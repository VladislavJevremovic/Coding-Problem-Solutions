# https://leetcode.com/problems/sliding-window-maximum/

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not n * k:  # any of them 0
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]


# TLE

def test():
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert s.maxSlidingWindow([9, 11], 2) == [11]
    assert s.maxSlidingWindow([4, -2], 2) == [4]
