# https://leetcode.com/problems/surrounded-regions/

from itertools import product
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(board: List[List[str]], row: int, col: int):
            if board[row][col] != 'O':
                return

            board[row][col] = 'E'
            if col < cols - 1:  # always check before recursion
                dfs(board, row, col + 1)
            if row < rows - 1:
                dfs(board, row + 1, col)
            if col > 0:
                dfs(board, row, col - 1)
            if row > 0:
                dfs(board, row - 1, col)

        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        # border cells
        borders = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))

        # mark the "escaped" cells ('O's on border and those 4-connected to them)
        for row, col in borders:
            dfs(board, row, col)

        # flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # captured
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # escaped


def test():
    s = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    board = [["X"]]
    s.solve(board)
    assert board == [["X"]]
