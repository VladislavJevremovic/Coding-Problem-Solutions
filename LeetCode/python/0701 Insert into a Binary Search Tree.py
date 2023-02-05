# https://leetcode.com/problems/insert-into-a-binary-search-tree


from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

# def test():
# def case(input: List[int], val: int, expected: List[int]) -> bool:
#
#     BinarySearchTree(Solution().insertIntoBST(BinarySearchTree.from_sequence(input).root, val))
#     BinarySearchTree.from_sequence(expected)
#
#     return input == expected
#
# assert case([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5])
# assert case([40, 20, 60, 10, 30, 50, 70], 25, [40, 20, 60, 10, 30, 50, 70, None, None, 25])
# assert case([4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [4, 2, 7, 1, 3, 5])
