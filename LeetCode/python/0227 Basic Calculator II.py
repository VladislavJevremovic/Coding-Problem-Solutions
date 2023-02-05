# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        stack = []
        current_number = 0
        operation = '+'  # previous
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                current_number = (current_number * 10) + (ord(c) - ord('0'))

            if c in ['+', '-', '*', '/'] or i == n - 1:  # new number is found, apply previous operation
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_number))

                operation = c
                current_number = 0

        result = 0
        while stack:
            result += stack.pop()

        return result


def test():
    s = Solution()
    assert s.calculate("3+2*2") == 7
    assert s.calculate(" 3/2 ") == 1
    assert s.calculate(" 3+5 / 2 ") == 5
    assert s.calculate("14-3/2") == 13
