# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Recursive preorder (node, left, right) built by list concatenation."""
        # Time: O(n^2)   Space: O(n)  (list concat at each node)
        if not root:
            return []

        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Iterative preorder using an explicit stack, pushing right before left
        so left is processed first."""
        # Time: O(n)   Space: O(n)
        result = []

        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:  # to process left 1st, push right 1st (popped later)
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


# Input: root = [1,None,2,3]
# Output: [1,2,3]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
#
# Input: root = [1,2]
# Output: [1,2]
# Example 5:
#
#
# Input: root = [1,None,2]
# Output: [1,2]


def test():
    def case(tree, expected: List[int]) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return (
            Solution1().preorderTraversal(root) == expected
            and Solution2().preorderTraversal(root) == expected
        )

    assert case([1, None, 2, 3], [1, 2, 3])
    assert case([], [])
    assert case([1], [1])
    assert case([1, 2], [1, 2])
