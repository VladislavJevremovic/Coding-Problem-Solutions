# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(bound=None):
            if not inorder or inorder[0] == bound:
                return None

            root = TreeNode(preorder.pop(0))  # start with root
            root.left = build(root.val)  # proceed left (as per preorder) with set pivot
            inorder.pop(0)
            root.right = build(bound)  # proceed right (as per preorder) with set bound

            return root

        return build()

# def test():
#     def case(list1: List[int], expected: List[int]) -> bool:
#         tree = BinarySearchTree.from_level_order_sequence(list1)
#         return Solution().levelOrder(tree.root) == expected if tree else not expected
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,None,None,15,7]
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
