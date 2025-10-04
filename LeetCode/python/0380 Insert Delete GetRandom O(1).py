# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
from typing import Any, List, Optional


class RandomizedSet:
    """Combine a list for O(1) random indexing with a value->index dict; deletion
    swaps the target with the last element so removal stays O(1)."""

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        # Time: O(1)   Space: O(1)
        if val in self.dict:
            return False

        self.dict[val] = len(self.list)  # value: insert_position
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        # Time: O(1)   Space: O(1)
        if val not in self.dict:
            return False

        last_element = self.list[-1]
        index_of_val = self.dict[val]
        self.list[index_of_val] = last_element  # move last element to val's position
        self.dict[last_element] = index_of_val  # and update dict accordingly

        self.list.pop()  # effectively shrink the list, popped may not be val
        del self.dict[val]

        return True

    def getRandom(self) -> int:
        # Time: O(1)   Space: O(1)
        return random.choice(self.list)


def test():
    def case(
        actions: List[str], params: List[List[int]], expected: List[List[Optional[Any]]]
    ) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "RandomizedSet":
                s = RandomizedSet()
                actual.append(None)
            elif action == "insert":
                actual.append(s.insert(param[0]))
            elif action == "remove":
                actual.append(s.remove(param[0]))
            elif action == "getRandom":
                actual.append(s.getRandom())

        return actual in expected

    assert case(
        [
            "RandomizedSet",
            "insert",
            "remove",
            "insert",
            "getRandom",
            "remove",
            "insert",
            "getRandom",
        ],
        [[], [1], [2], [2], [], [1], [2], []],
        [
            [None, True, False, True, 1, True, False, 2],
            [None, True, False, True, 2, True, False, 2],
        ],
    )
