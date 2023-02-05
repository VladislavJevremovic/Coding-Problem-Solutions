# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return

        m = len(board)
        n = len(board[0])
        if not m or not n:
            return

        x = [-1, -1, -1, 1, 1, 1, 0, 0]
        y = [-1, 0, 1, -1, 0, 1, 1, -1]

        for i in range(m):
            for j in range(n):
                c = 0
                for k in range(len(x)):
                    nx = i + x[k]
                    ny = j + y[k]
                    if 0 <= nx < m and 0 <= ny < n and (board[nx][ny] & 1 == 1):
                        c += 1

                if c < 2 and (board[i][j] & 1 == 1):
                    board[i][j] &= 0b01  # keep current, 0 next

                if (c == 2 or c == 3) and (board[i][j] & 1 == 1):
                    board[i][j] |= (board[i][j] << 1)  # keep current, copy 1 to next

                if c > 3 and (board[i][j] & 1 == 1):
                    board[i][j] &= 0b01  # keep current, 0 next

                if c == 3 and (board[i][j] & 1 == 0):
                    board[i][j] |= 0b10  # keep current, 1 next

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


def test():
    s = Solution()

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
