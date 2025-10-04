# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """Recursive: traverse left subtree, visit the node, then the right
        subtree, concatenating the results."""
        # Time: O(n)   Space: O(n) (recursion + concatenation)
        if not root:
            return []

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """Iterative with an explicit stack: push the leftmost spine, pop to
        visit, then descend into the right child."""
        # Time: O(n)   Space: O(n)
        result = []

        if not root:
            return result

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        tree = BinarySearchTree.from_level_order_sequence(list1)
        return (
            Solution1().inorderTraversal(tree.root) == expected
            if tree
            else not expected
        )

    assert case([1, None, 2, 3], [1, 3, 2])
    assert case([], [])
    assert case([1], [1])
    assert case([1, 2], [2, 1])
    assert case([1, None, 2], [1, 2])
