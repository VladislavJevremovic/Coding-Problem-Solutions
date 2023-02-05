# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node: TreeNode, arr: List[int], i: int) -> bool:
            if not node or i >= len(arr):
                return False

            if node.val != arr[i]:
                return False

            if (not node.left and not node.right) and i + 1 == len(arr):  # leaf?
                return True
            else:
                return dfs(node.left, arr, i + 1) or dfs(node.right, arr, i + 1)

        return dfs(root, arr, 0)

# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0
# Example 2:
#
#
#
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
# Example 3:
#
#
#
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,1]
# Output: false
