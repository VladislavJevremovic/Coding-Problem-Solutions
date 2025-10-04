# https://leetcode.com/problems/inorder-successor-in-bst/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """Descend the BST tracking the last node greater than p; when the walk
        ends that candidate is p's in-order successor."""
        # Time: O(h)   Space: O(1)
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor


# Input: root = [2,1,3], p = 1
# Output: 2
# Input: root = [5,3,6,2,4,None,None,1], p = 6
# Output: None


def test():
    def find(root, val):
        node = root
        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                return node
        return None

    def case(tree, p_val, expected):
        root = BinarySearchTree.from_level_order_sequence(tree).root
        p = find(root, p_val)
        successor = Solution().inorderSuccessor(root, p)
        if expected is None:
            assert successor is None
        else:
            assert successor.val == expected

    case([2, 1, 3], 1, 2)
    case([5, 3, 6, 2, 4, None, None, 1], 6, None)
