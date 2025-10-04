# https://leetcode.com/problems/transpose-matrix/

from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """Build the transpose so that out[j][i] = A[i][j] (m rows, n cols)."""
        # Time: O(m * n)   Space: O(m * n)
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def test():
    s = Solution()
    assert s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert s.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
