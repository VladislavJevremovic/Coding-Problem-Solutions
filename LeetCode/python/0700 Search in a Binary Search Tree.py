# https://leetcode.com/problems/search-in-a-binary-search-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:
            return root

        return self.searchBST(root.left, val) or self.searchBST(root.right, val)

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
