# https://leetcode.com/problems/last-stone-weight/

from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n < 1:
            return 0
        if n < 2:
            return stones[0]

        heap = [-stone for stone in stones]
        heapify(heap)
        remaining_stones = n
        while remaining_stones > 1:
            x = heappop(heap)
            y = heappop(heap)
            remaining_stones -= 2
            if x != y:
                heappush(heap, -abs(x - y))
                remaining_stones += 1

        return -heappop(heap) if heap else 0


def test():
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([2, 2]) == 0
