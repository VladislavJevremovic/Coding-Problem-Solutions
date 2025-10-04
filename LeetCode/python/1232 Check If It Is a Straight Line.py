# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """Take the first edge as a reference vector; all points are collinear iff
        each point's vector from the origin has zero cross product with it."""

        # Time: O(n)   Space: O(1)
        def makeVector(x: List[int], y: List[int]) -> List[int]:
            return [y[0] - x[0], y[1] - x[1]]

        def crossProduct(x: List[int], y: List[int]) -> int:
            return x[0] * y[1] - x[1] * y[0]

        if not coordinates:
            return False

        n = len(coordinates)
        if n <= 2:
            return True

        v1 = makeVector(coordinates[1], coordinates[0])
        for i in range(3, n):
            v2 = makeVector(coordinates[i], coordinates[0])
            if crossProduct(v1, v2):
                return False

        return True


def test():
    s = Solution()
    assert s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) is True
    assert (
        s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) is False
    )
