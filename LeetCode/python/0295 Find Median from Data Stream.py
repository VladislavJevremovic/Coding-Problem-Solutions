# https://leetcode.com/problems/find-median-from-data-stream/

from bisect import insort
from typing import List, Optional


class MedianFinder:
    """Keep the stream in a sorted list via binary insertion so the median is a
    direct middle-index lookup. n = number of elements stored."""

    def __init__(self):
        self.store = list()

    def addNum(self, num: int) -> None:
        # Time: O(n) for the shift after binary search   Space: O(1)
        if not self.store:
            self.store.append(num)
        else:
            insort(self.store, num)

    def findMedian(self) -> float:
        # Time: O(1)   Space: O(1)
        n = len(self.store)

        if n % 2 == 1:
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) * 0.5


def test():
    def case(
        actions: List[str], params: List[List[int]], expected: List[Optional[float]]
    ) -> bool:
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
        [None, None, None, 1.5, None, 2.0],
    )
