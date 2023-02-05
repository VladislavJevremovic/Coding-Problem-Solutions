# https://leetcode.com/problems/lru-cache/
from typing import List

from python.Helpers.DoublyLinkedList import *


class LRUCache:
    def __init__(self, capacity):
        self.list = DoublyLinkedList()
        self.cache = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.list.move_node_to_head(node)

        return node.value

    def put(self, key, value):
        node = self.cache.get(key, None)
        if not node:
            new_node = DoublyLinkedNode(key, value)

            self.cache[key] = new_node
            self.list.add_node_to_head(new_node)

            self.size += 1
            if self.size > self.capacity:
                tail = self.list.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.list.move_node_to_head(node)


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "LRUCache":
                s = LRUCache(param[0])
                actual.append(None)
            elif action == "put":
                s.put(param[0], param[1])
                actual.append(None)
            elif action == "get":
                actual.append(s.get(param[0]))

        return actual == expected

    assert case(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        [None, None, None, 1, None, -1, None, -1, 3, 4]
    )
