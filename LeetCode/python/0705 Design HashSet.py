# https://leetcode.com/problems/design-hashset/

from collections import defaultdict
from typing import List, Optional


class MyHashSet:
    def __init__(self):
        self.hash_map = defaultdict(bool)

    def add(self, key: int) -> None:
        self.hash_map[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hash_map[key]

    def contains(self, key: int) -> bool:
        return self.hash_map[key]


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[bool]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MyHashSet":
                s = MyHashSet()
                actual.append(None)
            elif action == "add":
                s.add(param[0])
                actual.append(None)
            elif action == "contains":
                actual.append(s.contains(param[0]))
            elif action == "remove":
                s.remove(param[0])
                actual.append(None)

        return actual == expected

    assert case(
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
        [None, None, None, True, False, None, True, None, False]
    )
