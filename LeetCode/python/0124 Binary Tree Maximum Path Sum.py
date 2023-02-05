# https://leetcode.com/problems/binary-tree-maximum-path-sum/

import math

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def __init__(self):
        self.result = -math.inf

    def maxPathSum(self, root: TreeNode) -> int:
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
