# https://leetcode.com/problems/binary-tree-maximum-path-sum/

import math

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def __init__(self):
        self.result = -math.inf

    def maxPathSum(self, root: TreeNode) -> int:
        """Post-order recursion: each node returns the best downward path it can
        extend, while tracking the best path that bends through any node."""

        # Time: O(n)   Space: O(h)
        def sum(node: TreeNode) -> int:
            if not node:
                return 0

            left_sum = sum(node.left)
            right_sum = sum(node.right)

            # current node may be temp root or on result path

            temp_max = node.val + max(0, left_sum, right_sum, left_sum + right_sum)
            self.result = max(self.result, temp_max)

            return node.val + max(0, left_sum, right_sum)

        sum(root)

        return self.result


# Input: root = [1,2,3]
# Output: 6
#
# Input: root = [-10,9,20,None,None,15,7]
# Output: 42


def test():
    def case(tree, expected: int) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().maxPathSum(root) == expected

    assert case([1, 2, 3], 6)
    assert case([-10, 9, 20, None, None, 15, 7], 42)
    assert case([-3], -3)
