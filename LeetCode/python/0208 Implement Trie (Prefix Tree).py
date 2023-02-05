# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict
from typing import List, Optional


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)  # {char: Trie}
        self.isWord = False

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            current = current.children[c]  # creates child if None
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c not in current.children:
                return False
            current = current.children.get(c)  # doesn't create child if None

        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children.get(c)  # doesn't create child if None

        return True


def test():
    def case(actions: List[str], params: List[List[str]], expected: List[Optional[bool]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "Trie":
                s = Trie()
                actual.append(None)
            elif action == "insert":
                s.insert(param[0])
                actual.append(None)
            elif action == "search":
                actual.append(s.search(param[0]))
            elif action == "startsWith":
                actual.append(s.startsWith(param[0]))

        return actual == expected

    assert case(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        [None, None, True, False, True, None, True]
    )
