# https://leetcode.com/problems/reshape-the-matrix/

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if not m or m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]
        count = 0
        for i in range(m):
            for j in range(n):
                result[count // c][count % c] = mat[i][j]
                count += 1

        return result


def test():
    s = Solution()
    assert s.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert s.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
