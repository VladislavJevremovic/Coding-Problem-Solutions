# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s=[], left=0, right=0):
            if len(s) == 2 * n:
                result.append("".join(s))
                return

            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()

            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()

        result = []
        backtrack()

        return result


def test():
    s = Solution()
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
