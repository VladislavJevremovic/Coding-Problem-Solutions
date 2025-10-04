# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution1:  # O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Staircase walk from the bottom-left: move right when the cell is too
        small, up when too large."""
        # Time: O(m + n)   Space: O(1)
        m = len(matrix)
        n = len(matrix[0])

        x, y = m - 1, 0
        while x >= 0 and y <= n - 1:
            c = matrix[x][y]
            if c == target:
                return True
            elif c < target:
                y += 1
            else:
                x -= 1

        return False


class Solution2:  # O(logmn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Binary search treating the row-major matrix as one sorted array,
        mapping a flat index back to (row, col)."""
        # Time: O(log(m * n))   Space: O(1)
        m = len(matrix)
        n = len(matrix[0])

        x, y = 0, m * n - 1
        while x <= y:
            mid = x + (y - x) // 2
            c = matrix[mid // n][mid % n]
            if c == target:
                return True
            elif c < target:
                x += 1
            else:
                y -= 1

        return False


def test():
    s = Solution2()
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert (
        s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    )
