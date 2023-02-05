# https://leetcode.com/problems/inorder-successor-in-bst/

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor

# Input: root = [2,1,3], p = 1
# Output: 2
# Input: root = [5,3,6,2,4,None,None,1], p = 6
# Output: None
