# https://leetcode.com/problems/diameter-of-binary-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Post-order recursion returning each node's height and best diameter;
        the diameter through a node is the sum of its two child heights."""

        # Time: O(n)   Space: O(h)   (recursion stack; h = tree height)
        def heightAndDiameter(node) -> (int, int):
            if not node:
                return 0, 0

            h1, d1 = heightAndDiameter(node.left)
            h2, d2 = heightAndDiameter(node.right)

            return 1 + max(h1, h2), max(d1, d2, h1 + h2)

        return heightAndDiameter(root)[1]


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
#
# Input: root = [1,2]
# Output: 1


def test():
    def case(tree, expected: int) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().diameterOfBinaryTree(root) == expected

    assert case([1, 2, 3, 4, 5], 3)
    assert case([1, 2], 1)
    assert case([], 0)
    assert case([1], 0)
