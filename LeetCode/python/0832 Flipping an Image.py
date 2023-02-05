# https://leetcode.com/problems/flipping-an-image

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(A)
        for row in A:
            new_row = []
            for j in range(n):
                new_row.append(1 - row[n - j - 1])
            result.append(new_row)

        return result


def test():
    s = Solution()
    assert s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == [[1, 1, 0, 0],
                                                                                              [0, 1, 1, 0],
                                                                                              [0, 0, 0, 1],
                                                                                              [1, 0, 1, 0]]
