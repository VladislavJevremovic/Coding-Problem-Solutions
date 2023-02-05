# https://leetcode.com/problems/find-median-from-data-stream/

from bisect import insort
from typing import List, Optional


class MedianFinder:
    def __init__(self):
        self.store = list()

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            insort(self.store, num)

    def findMedian(self) -> float:
        n = len(self.store)

        if n % 2 == 1:
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) * 0.5


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[float]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MedianFinder":
                s = MedianFinder()
                actual.append(None)
            elif action == "addNum":
                s.addNum(param[0])
                actual.append(None)
            elif action == "findMedian":
                actual.append(s.findMedian())

        return actual == expected

    assert case(
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []],
        [None, None, None, 1.5, None, 2.0]
    )
