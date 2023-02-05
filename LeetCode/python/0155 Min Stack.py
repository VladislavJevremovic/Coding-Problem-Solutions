# https://leetcode.com/problems/min-stack/

from typing import Optional, List


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            min_value = x
        else:
            min_value = min(x, self.getMin())
        self.stack.append((x, min_value))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            (v, m) = self.stack[-1]
            return v
        else:
            return 0

    def getMin(self) -> int:
        if self.stack:
            (v, m) = self.stack[-1]
            return m
        else:
            return 0


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MinStack":
                s = MinStack()
                actual.append(None)
            elif action == "push":
                s.push(param[0])
                actual.append(None)
            elif action == "pop":
                s.pop()
                actual.append(None)
            elif action == "top":
                actual.append(s.top())
            elif action == "getMin":
                actual.append(s.getMin())

        return actual == expected

    assert case(
        ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        [[], [-2], [0], [-3], [], [], [], []],
        [None, None, None, None, -3, None, 0, -2]
    )
