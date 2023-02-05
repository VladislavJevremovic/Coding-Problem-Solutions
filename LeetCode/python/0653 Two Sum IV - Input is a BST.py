# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root: Optional[TreeNode], k: int, d: List[int]):
            if not root:
                return False

            if (k - root.val) in d:
                return True

            d.append(root.val)

            return dfs(root.left, k, d) or dfs(root.right, k, d)

        return dfs(root, k, [])

# Input: root = [5,3,6,2,4,None,7], k = 9
# Output: true
# Example 2:
#
#
# Input: root = [5,3,6,2,4,None,7], k = 28
# Output: false
# Example 3:
#
# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:
#
# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:
#
# Input: root = [2,1,3], k = 3
# Output: true
