# https://leetcode.com/problems/same-tree/
from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


def test():
    def case(list1: List[int], list2: List[int], expected: bool) -> bool:
        return Solution().isSameTree(
            BinarySearchTree.from_level_order_sequence(list1).root,
            BinarySearchTree.from_level_order_sequence(list2).root
        ) is expected

    assert case([1, 2, 3], [1, 2, 3], True)
    assert case([1, 2], [1, None, 2], False)
    assert case([1, 2, 1], [1, 1, 2], False)
