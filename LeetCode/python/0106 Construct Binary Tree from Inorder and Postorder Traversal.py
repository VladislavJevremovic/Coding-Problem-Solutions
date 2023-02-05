# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(bound=None):
            if not inorder or inorder[-1] == bound:
                return None

            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)

            return root

        return build()

# def test():
#     def case(list1: List[int], expected: List[int]) -> bool:
#         tree = BinarySearchTree.from_level_order_sequence(list1)
#         return Solution().levelOrder(tree.root) == expected if tree else not expected
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,None,None,15,7]
# Example 2:
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
