# https://leetcode.com/problems/cousins-in-binary-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def depthAndParentValue(root: TreeNode, x: int, depth: int, parent: int) -> (int, int):
            if not root:
                return None

            if root.val == x:
                return depth, parent

            left = depthAndParentValue(root.left, x, depth + 1, root.val)
            right = depthAndParentValue(root.right, x, depth + 1, root.val)

            return left if left else right

        (x_depth, x_parent_value) = depthAndParentValue(root, x, 0, 0)
        (y_depth, y_parent_value) = depthAndParentValue(root, y, 0, 0)

        return x_depth == y_depth and x_parent_value != y_parent_value

# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Input: root = [1,2,3,None,4,None,5], x = 5, y = 4
# Output: true
#
# Input: root = [1,2,3,None,4], x = 2, y = 3
# Output: false
