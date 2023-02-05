# https://leetcode.com/problems/binary-tree-paths/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        r = []
        stack = [[root, str(root.val)]]
        while stack:
            node, path = stack.pop()

            if node.left:
                stack.append([node.left, path + '->' + str(node.left.val)])

            if node.right:
                stack.append([node.right, path + '->' + str(node.right.val)])

            if not node.left and not node.right:
                r.append(path)

        return r

# def test():
# Input: root = [1,2,3,None,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"]
