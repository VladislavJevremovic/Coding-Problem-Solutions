# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
# HackerRank: Queue using Two Stacks
from typing import List


class Queue:
    """FIFO queue backed by two LIFO stacks; dequeues drain the in-stack into the out-stack."""

    # enqueue: O(1)   dequeue: O(1) amortized   front: O(1) amortized   Space: O(n)

    def __init__(self) -> None:
        self._in: List[int] = []
        self._out: List[int] = []

    def enqueue(self, value: int) -> None:
        self._in.append(value)

    def _shift(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def dequeue(self) -> int:
        self._shift()
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def front(self) -> int:
        self._shift()
        if not self._out:
            raise IndexError("front from empty queue")
        return self._out[-1]


def test() -> None:
    q = Queue()
    q.enqueue(42)
    assert q.dequeue() == 42
    q.enqueue(14)
    assert q.front() == 14
    q.enqueue(28)
    assert q.front() == 14
    q.enqueue(60)
    q.enqueue(78)
    assert q.dequeue() == 14
    assert q.dequeue() == 28
    assert q.front() == 60
    # front does not remove
    assert q.front() == 60
    assert q.dequeue() == 60
    assert q.dequeue() == 78
