# https://leetcode.com/problems/invert-binary-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = [root]
        while queue:
            current = queue.pop()
            temp = current.left
            current.left = current.right
            current.right = temp

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
# Input: root = []
# Output: []
