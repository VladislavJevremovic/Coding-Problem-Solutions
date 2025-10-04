# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
from typing import List


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Sort all points by squared distance and take the first k."""
        # Time: O(n log n)   Space: O(n)
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Heapify all points by distance, then pop the k smallest."""
        # Time: O(n + k log n)   Space: O(n)
        r = []

        if not points:
            return r

        pd = [((point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(pd)

        for _ in range(k):
            p = heapq.heappop(pd)[1]
            r.append(p)

        return r


class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Keep a size-k max-heap (negated distances) of the closest points seen
        so far, evicting the farthest as new points arrive."""
        # Time: O(n log k)   Space: O(k)
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [[x, y] for (dist, x, y) in heap]


def test():
    def case(points: List[List[int]], K: int, expected: List[List[int]]) -> bool:
        return sorted(Solution3().kClosest(points, K)) == sorted(expected)

    assert case([[1, 3], [-2, 2]], 1, [[-2, 2]])
    assert case([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]])
