# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:  # to process left 1st, push right 1st (popped later)
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

# Input: root = [1,None,2,3]
# Output: [1,2,3]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
#
# Input: root = [1,2]
# Output: [1,2]
# Example 5:
#
#
# Input: root = [1,None,2]
# Output: [1,2]
