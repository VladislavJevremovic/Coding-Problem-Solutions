# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_depth = (1 + self.minDepth(root.left)) if root.left else float("inf")
        right_depth = (1 + self.minDepth(root.right)) if root.right else float("inf")

        return min(left_depth, right_depth)

# Input: root = [3,9,20,None,None,15,7]
# Output: 2
#
# Input: root = [2,None,3,None,4,None,5,None,6]
# Output: 5
