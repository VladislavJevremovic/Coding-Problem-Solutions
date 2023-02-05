# https://leetcode.com/problems/binary-tree-level-order-traversal/

import collections
from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        q = collections.deque([root])

        level = []
        while q:
            c = len(q)
            for _ in range(c):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            levels.append(level)
            level = []

        return levels


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        tree = BinarySearchTree.from_level_order_sequence(list1)
        return Solution().levelOrder(tree.root) == expected if tree else not expected

    assert case([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
    assert case([1], [[1]])
    assert case([], [])
