# https://leetcode.com/problems/merge-two-binary-trees/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            tmp = TreeNode(t1.val + t2.val)
            tmp.left = self.mergeTrees(t1.left, t2.left)
            tmp.right = self.mergeTrees(t1.right, t2.right)

            return tmp

# Input: root1 = [1,3,2,5], root2 = [2,1,3,None,4,None,7]
# Output: [3,4,5,5,4,None,7]
# Example 2:
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
