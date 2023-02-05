# https://leetcode.com/problems/first-unique-number/

from collections import deque
from typing import List, Optional


class FirstUnique:
    def __init__(self, nums: List[int]):
        self._queue = deque([])  # error in official solution, no need for nums here
        self._is_unique = {}

        for num in nums:  # process for _is_unique
            self.add(num)

    def showFirstUnique(self) -> int:
        while self._queue and not self._is_unique[self._queue[0]]:  # purge
            self._queue.popleft()

        if self._queue:
            return self._queue[0]

        return -1

    def add(self, value: int) -> None:
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue.append(value)
        else:
            self._is_unique[value] = False


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "FirstUnique":
                s = FirstUnique(param[0])
                actual.append(None)
            elif action == "showFirstUnique":
                actual.append(s.showFirstUnique())
            elif action == "add":
                s.add(param[0])
                actual.append(None)

        return actual == expected

    assert case(
        ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add",
         "showFirstUnique"],
        [[[2, 3, 5]], [], [5], [], [2], [], [3], []],
        [None, 2, None, 2, None, 3, None, -1]
    )
    assert case(
        ["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"],
        [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []],
        [None, -1, None, None, None, None, None, 17]
    )
    assert case(
        ["FirstUnique", "showFirstUnique", "add", "showFirstUnique"],
        [[[809]], [], [809], []],
        [None, 809, None, -1]
    )
