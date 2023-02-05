# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        t = [-num for num in nums]
        heapq.heapify(t)

        return -[heapq.heappop(t) for _ in range(k)][-1]


def test():
    s = Solution3()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
