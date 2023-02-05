# https://leetcode.com/problems/max-points-on-a-line/

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a: int, b: int) -> int:
            return a if not b else gcd(b, a % b)

        if not points:
            return 0

        n = len(points)
        if n <= 2:
            return n

        result = 0
        for i in range(n):
            map = {}  # { (x, y): number_of_points_on_line_defined_by_slope_y/x }
            overlap = 0
            maximum = 0
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if not dx and not dy:
                    overlap += 1
                    continue

                gcd_dx_dy = gcd(dx, dy)
                if gcd_dx_dy:
                    dx /= gcd_dx_dy
                    dy /= gcd_dx_dy

                line = (dx, dy)
                map[line] = map[line] + 1 if line in map else 1
                maximum = max(maximum, map[line])

            result = max(result, maximum + overlap + 1)

        return result


def test():
    s = Solution()
    assert s.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
