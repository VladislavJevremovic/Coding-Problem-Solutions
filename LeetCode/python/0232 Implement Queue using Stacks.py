# https://leetcode.com/problems/implement-queue-using-stacks/

from typing import Any, List, Optional


class MyQueue:
    """FIFO queue backed by two LIFO stacks: pushes land on an input stack and
    are lazily reversed onto an output stack so the front can be read/removed."""

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Time: O(1)   Space: O(1)
        self.stack1.append(x)

    def pop(self) -> int:
        # Time: O(1) amortized   Space: O(1)
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        # Time: O(1) amortized   Space: O(1)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        # Time: O(1)   Space: O(1)
        return not self.stack1 and not self.stack2


def test():
    def case(
        actions: List[str], params: List[List[int]], expected: List[Optional[Any]]
    ) -> bool:
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
        [None, None, None, 1, 1, False],
    )
