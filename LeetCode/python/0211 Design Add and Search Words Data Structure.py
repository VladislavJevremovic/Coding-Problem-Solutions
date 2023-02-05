# https://leetcode.com/problems/add-and-search-word-data-structure-design/

from collections import defaultdict
from typing import List, Optional


class WordDictionary:
    class Node:
        def __init__(self):
            self.children = defaultdict(WordDictionary.Node)  # {char: Node}
            self.is_leaf = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children[c]  # creates child if None
        current.is_leaf = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary.Node, level: int):
            if level == len(word):
                return node.is_leaf

            c = word[level]

            if c == ".":
                for child in node.children:
                    if dfs(node.children[child], level + 1):
                        return True

            if c in node.children:
                return dfs(node.children[c], level + 1)

            return False

        return dfs(self.root, 0)


def test():
    def case(actions: List[str], params: List[List[str]], expected: List[Optional[bool]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "WordDictionary":
                s = WordDictionary()
                actual.append(None)
            elif action == "addWord":
                s.addWord(param[0])
                actual.append(None)
            elif action == "search":
                actual.append(s.search(param[0]))

        return actual == expected

    assert case(
        ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
        [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
        [None, None, None, None, False, True, True, True]
    )
