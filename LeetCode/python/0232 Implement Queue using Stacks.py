# https://leetcode.com/problems/implement-queue-using-stacks/

from typing import List, Optional, Any


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[Any]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MyQueue":
                s = MyQueue()
                actual.append(None)
            elif action == "push":
                s.push(param[0])
                actual.append(None)
            elif action == "peek":
                actual.append(s.peek())
            elif action == "pop":
                actual.append(s.pop())
            elif action == "empty":
                actual.append(s.empty())

        return actual == expected

    assert case(
        ["MyQueue", "push", "push", "peek", "pop", "empty"],
        [[], [1], [2], [], [], []],
        [None, None, None, 1, 1, False]
    )
