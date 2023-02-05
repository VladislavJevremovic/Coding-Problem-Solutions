# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for row in range(1, numRows):
            new_row = [1]
            for i in range(row - 1):
                new_row.append(result[-1][i] + result[-1][i + 1])
            new_row.append(1)

            result.append(new_row)

        return result


def test():
    s = Solution()
    assert s.generate(1) == [[1]]
    assert s.generate(2) == [[1], [1, 1]]
    assert s.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert s.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
