# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Sort ascending and index the k-th element from the end."""
        # Time: O(n log n)   Space: O(n)
        return sorted(nums)[-k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Take the k largest via a heap and return the smallest of them."""
        # Time: O(n log k)   Space: O(k)
        return heapq.nlargest(k, nums)[-1]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Build a min-heap of negated values and pop k times so the k-th pop is
        the k-th largest original value."""
        # Time: O(n + k log n)   Space: O(n)
        t = [-num for num in nums]
        heapq.heapify(t)

        return -[heapq.heappop(t) for _ in range(k)][-1]


def test():
    s = Solution3()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
