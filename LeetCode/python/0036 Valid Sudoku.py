# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]
        boxs = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v == ".":
                    continue

                if v in rows[i]:
                    return False
                rows[i].append(v)

                if v in cols[j]:
                    return False
                cols[j].append(v)

                ix = (i // 3) * 3 + j // 3
                if v in boxs[ix]:
                    return False
                boxs[ix].append(v)

        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [0] * n
        cols = [0] * n
        boxs = [0] * n

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue

                p = int(board[i][j]) - 1  # 0-8, 9 bit positions

                if rows[i] & (1 << p):
                    return False
                rows[i] |= (1 << p)

                if cols[j] & (1 << p):
                    return False
                cols[j] |= (1 << p)

                ix = (i // 3) * 3 + j // 3
                if boxs[ix] & (1 << p):
                    return False
                boxs[ix] |= (1 << p)

        return True


def test():
    s = Solution2()
    assert s.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True
    assert s.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
