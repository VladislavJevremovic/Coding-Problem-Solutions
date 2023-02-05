# https://leetcode.com/problems/validate-binary-search-tree/

import math
from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTInRange(root: TreeNode, a: float, b: float) -> bool:
            if not root:
                return True

            if root.val <= a or root.val >= b:
                return False

            return isValidBSTInRange(root.left, a, root.val) and isValidBSTInRange(root.right, root.val, b)

        return isValidBSTInRange(root, -float("inf"), float("inf"))


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def isNodeInRange(root: TreeNode, a: int, b: int) -> bool:
            if not root:
                return True

            if a >= root.val or root.val >= b:
                return False

            return isNodeInRange(root.left, a, root.val) and isNodeInRange(root.right, root.val, b)

        return isNodeInRange(root, -math.inf, math.inf)


def test():
    def case(list1: List[int], expected: bool) -> bool:
        return Solution1().isValidBST(BinarySearchTree.from_level_order_sequence(list1).root) is expected

    assert case([2, 1, 3], True)
    assert case([5, 1, 4, None, None, 3, 6], False)
