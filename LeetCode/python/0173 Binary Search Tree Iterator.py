# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import List, Any

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def in_order(root: Optional[TreeNode]) -> List[int]:
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []

        self.nodes = in_order(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes)


def test():
    def case(actions: List[str], params: List[List[Optional[int]]], expected: List[Optional[Any]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "BSTIterator":
                s = BSTIterator(BinarySearchTree.from_level_order_sequence(param[0]).root)
                actual.append(None)
            elif action == "next":
                actual.append(s.next())
            elif action == "hasNext":
                actual.append(s.hasNext())

        return actual == expected

    assert case(
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
        [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []],
        [None, 3, 7, True, 9, True, 15, True, 20, False]
    )
