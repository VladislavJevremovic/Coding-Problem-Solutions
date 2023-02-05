# https://leetcode.com/problems/design-hashmap/
from typing import List, Optional


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v

        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):
    def __init__(self):
        self.key_space = 2069  # prime is better (if a lesser divisor exists, then only a fraction of key space is used)
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MyHashMap":
                s = MyHashMap()
                actual.append(None)
            elif action == "put":
                s.put(param[0], param[1])
                actual.append(None)
            elif action == "get":
                actual.append(s.get(param[0]))
            elif action == "remove":
                s.remove(param[0])
                actual.append(None)

        return actual == expected

    assert case(
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
        [None, None, None, 1, -1, None, 1, None, -1]
    )
