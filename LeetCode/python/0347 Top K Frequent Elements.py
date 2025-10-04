# https://leetcode.com/problems/top-k-frequent-elements/

import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Count frequencies, then pop the k most frequent off a max-heap keyed
        by negated count."""
        # Time: O(n + k log n)   Space: O(n)
        counts = collections.Counter(nums)
        t = [(-count, num) for num, count in counts.items()]
        heapq.heapify(t)

        return [heapq.heappop(t)[1] for _ in range(k)]


def test():
    s = Solution()
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
