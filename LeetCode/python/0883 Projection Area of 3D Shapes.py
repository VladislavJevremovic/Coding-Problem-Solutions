# https://leetcode.com/problems/projection-area-of-3d-shapes/

from typing import List


class Solution1:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """Single nested pass accumulating the top shadow plus, per row, the row
        and column maxima for the side projections (n = grid side)."""
        # Time: O(n^2)   Space: O(1)
        n = len(grid)
        result = 0

        for i in range(n):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(n):
                if grid[i][j]:
                    result += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            result += best_row + best_col

        return result


class Solution2:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """Sum the three projections functionally: row maxima, column maxima
        (via zip transpose), and the count of nonzero cells."""
        # Time: O(n^2)   Space: O(n)
        hor = sum(map(max, grid))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)

        return ver + hor + top


def test():
    s = Solution1()
    assert s.projectionArea([[1, 2], [3, 4]]) == 17
    assert s.projectionArea([[2]]) == 5
    assert s.projectionArea([[1, 0], [0, 2]]) == 8
    assert s.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14
    assert s.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 21
