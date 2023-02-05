# https://leetcode.com/problems/path-sum-ii/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, remainder, current_path, result):
            if not node:
                return

            current_path.append(node.val)
            if remainder == node.val and not node.left and not node.right:
                result.append(current_path[:])
            else:
                backtrack(node.left, remainder - node.val, current_path, result)
                backtrack(node.right, remainder - node.val, current_path, result)

            current_path.pop()

        result = []
        backtrack(root, targetSum, [], result)

        return result

# Input: root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Input: root = [1,2], targetSum = 0
# Output: []
