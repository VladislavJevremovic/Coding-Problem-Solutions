# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        """Push opening brackets onto a stack; on each closing bracket the top
        of the stack must be its matching opener."""
        # Time: O(n)   Space: O(n)
        stack = []
        d = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in d:
                if not stack:
                    return False
                if stack.pop() != d[c]:
                    return False
            else:
                stack.append(c)

        return not stack


def test():
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
