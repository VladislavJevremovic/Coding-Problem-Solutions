# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        size = len(preorder)
        if not preorder or not size:
            return None

        stack = []

        i = 0
        root = TreeNode(preorder[i])
        stack.append(root)
        i += 1

        while i < size:
            temp = None
            while len(stack) and preorder[i] > stack[-1].val:
                temp = stack.pop()

            if temp:
                temp.right = TreeNode(preorder[i])
                stack.append(temp.right)
            else:
                temp = stack[-1]
                temp.left = TreeNode(preorder[i])
                stack.append(temp.left)

            i += 1

        return root

# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,None,12]
#
# Input: preorder = [1,3]
# Output: [1,None,3]
