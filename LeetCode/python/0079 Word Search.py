# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x: int, y: int, suffix):
            if not len(suffix):
                return True

            if x < 0 or x > rows - 1 or y < 0 or y > cols - 1 or board[x][y] != suffix[0]:
                return False

            board[x][y] = '#'
            for d_x, d_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                result = backtrack(x + d_x, y + d_y, suffix[1:])
                if result:
                    break
            # revert the change
            board[x][y] = suffix[0]

            return result

        rows = len(board)
        cols = len(board[0])

        for x in range(rows):
            for y in range(cols):
                if backtrack(x, y, word):
                    return True

        return False


def test():
    s = Solution()
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    assert s.exist(board, "ABCCED") is True
    assert s.exist(board, "SEE") is True
    assert s.exist(board, "ABCB") is False
