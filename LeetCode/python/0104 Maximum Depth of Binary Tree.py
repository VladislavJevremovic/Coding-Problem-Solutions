# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# def test():
#     def case(list1: List[int], expected: List[int]) -> bool:
#         tree = BinarySearchTree.from_level_order_sequence(list1)
#         return Solution().levelOrder(tree.root) == expected if tree else not expected
# Input: root = [3,9,20,None,None,15,7]
# Output: 3
# Example 2:
#
# Input: root = [1,None,2]
# Output: 2
# Example 3:
#
# Input: root = []
# Output: 0
# Example 4:
#
# Input: root = [0]
# Output: 1
