# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluate postfix notation with a stack: push numbers, and on an
        operator pop the two operands and push the result."""
        # Time: O(n)   Space: O(n)
        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack.pop()


def test():
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )
