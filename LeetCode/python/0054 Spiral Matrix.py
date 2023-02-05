# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result

        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            if c1 <= c2:
                for c in range(c1, c2 + 1):
                    result.append(matrix[r1][c])

            if r1 + 1 <= r2:
                for r in range(r1 + 1, r2 + 1):
                    result.append(matrix[r][c2])

            if r1 < r2 and c1 < c2:
                if c1 + 1 <= c2 - 1:
                    for c in reversed(range(c1 + 1, c2)):
                        result.append(matrix[r2][c])

                if r1 + 1 <= r2:
                    for r in reversed(range(r1 + 1, r2 + 1)):
                        result.append(matrix[r][c1])

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return result


def test():
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
