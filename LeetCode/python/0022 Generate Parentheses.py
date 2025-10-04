# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Backtrack, adding '(' while opens remain and ')' only while it keeps
        the prefix valid (right < left)."""

        # Time: O(4^n / sqrt(n))   Space: O(n) recursion depth
        def backtrack(s=None, left=0, right=0):
            if s is None:
                s = []
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
    assert s.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    assert s.generateParenthesis(1) == ["()"]
