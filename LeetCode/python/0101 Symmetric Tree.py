# https://leetcode.com/problems/symmetric-tree/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrored(root, root)

    def isMirrored(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:  # here at least 1 not None
            return False

        return t1.val == t2.val and self.isMirrored(t1.right, t2.left) and self.isMirrored(t1.left, t2.right)


def test():
    def case(list1: List[int], expected: bool) -> bool:
        return Solution().isSymmetric(BinarySearchTree.from_level_order_sequence(list1).root) is expected

    assert case([1, 2, 2, 3, 4, 4, 3], True)
    assert case([1, 2, 2, None, 3, None, 3], False)
