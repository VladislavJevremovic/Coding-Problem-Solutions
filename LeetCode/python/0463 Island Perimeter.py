# https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = 0
        adjacent = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        adjacent += 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        adjacent += 1

        return 4 * land - 2 * adjacent


def test():
    s = Solution()
    assert s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    assert s.islandPerimeter([[1]]) == 4
    assert s.islandPerimeter([[1, 0]]) == 4
