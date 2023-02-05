# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node) -> bool:
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            current = current_node == p or current_node == q

            # if two of three True, found it
            if current + left + right >= 2:
                self.result = current_node

            return current or left or right

        recurse_tree(root)

        return self.result

# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
# Output: 3
#
# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
# Output: 5
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
