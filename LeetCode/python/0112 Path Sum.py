# https://leetcode.com/problems/path-sum/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right

# Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
# Output: true
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: false
