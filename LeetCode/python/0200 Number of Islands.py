# https://leetcode.com/problems/number-of-islands

from typing import List


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsClearIsland(grid: List[List[str]], i: int, j: int):
            if grid[i][j] == "1":
                grid[i][j] = "0"

                if i - 1 >= 0:
                    dfsClearIsland(grid, i - 1, j)
                if i + 1 < len(grid):
                    dfsClearIsland(grid, i + 1, j)
                if j - 1 >= 0:
                    dfsClearIsland(grid, i, j - 1)
                if j + 1 < len(grid[0]):
                    dfsClearIsland(grid, i, j + 1)

        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    r += 1
                    dfsClearIsland(grid, i, j)

        return r


class Solution2:
    def removeIslandDFS(self, grid, i, j):
        if grid[i][j] == '1':
            grid[i][j] = '0'
            if i + 1 <= len(grid) - 1:
                self.removeIslandDFS(grid, i + 1, j)
            if i - 1 >= 0:
                self.removeIslandDFS(grid, i - 1, j)
            if j + 1 <= len(grid[i]) - 1:
                self.removeIslandDFS(grid, i, j + 1)
            if j - 1 >= 0:
                self.removeIslandDFS(grid, i, j - 1)

    def removeIslandBFS(self, grid, i, j):
        q = [[i, j]]
        while q:
            index = q.pop(0)
            row = index[0]
            col = index[1]

            if grid[row][col] == '1':
                grid[row][col] = '0'

                if row + 1 <= len(grid) - 1:
                    q.append([row + 1, col])
                if row - 1 >= 0:
                    q.append([row - 1, col])
                if col + 1 <= len(grid[row]) - 1:
                    q.append([row, col + 1])
                if col - 1 >= 0:
                    q.append([row, col - 1])

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    self.removeIslandBFS(grid, i, j)

        return res


def test():
    s = Solution1()
    assert s.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

    assert s.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
