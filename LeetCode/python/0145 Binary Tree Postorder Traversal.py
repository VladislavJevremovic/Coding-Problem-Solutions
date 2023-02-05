# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.insert(0, node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result

# Input: root = [1,None,2,3]
# Output: [3,2,1]
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
# Output: [2,1]
# Example 5:
#
#
# Input: root = [1,None,2]
# Output: [2,1]
