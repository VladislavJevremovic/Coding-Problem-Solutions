# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:
    def islandAreaDFS(self, grid: List[List[int]], i: int, j: int) -> int:
        """Flood-fill from (i, j), sinking visited land and returning the area
        of the connected island."""
        # Time: O(m * n)   Space: O(m * n)   (recursion stack)
        a = 0
        if grid[i][j]:
            a += 1
            grid[i][j] = 0

            if i - 1 >= 0:
                a += self.islandAreaDFS(grid, i - 1, j)
            if i + 1 < len(grid):
                a += self.islandAreaDFS(grid, i + 1, j)
            if j - 1 >= 0:
                a += self.islandAreaDFS(grid, i, j - 1)
            if j + 1 < len(grid[0]):
                a += self.islandAreaDFS(grid, i, j + 1)

        return a

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Run a flood fill from each land cell and keep the largest island
        area found."""
        # Time: O(m * n)   Space: O(m * n)   (recursion stack)
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    a = self.islandAreaDFS(grid, i, j)
                    r = max(r, a)

        return r


def test():
    s = Solution()
    assert (
        s.maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
        == 6
    )
    assert s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
