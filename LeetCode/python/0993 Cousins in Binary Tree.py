# https://leetcode.com/problems/cousins-in-binary-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """Find each value's depth and parent via DFS; they are cousins iff the
        depths match but the parents differ."""

        # Time: O(n)   Space: O(h)
        def depthAndParentValue(
            root: TreeNode, x: int, depth: int, parent: int
        ) -> (int, int):
            if not root:
                return None

            if root.val == x:
                return depth, parent

            left = depthAndParentValue(root.left, x, depth + 1, root.val)
            right = depthAndParentValue(root.right, x, depth + 1, root.val)

            return left if left else right

        (x_depth, x_parent_value) = depthAndParentValue(root, x, 0, 0)
        (y_depth, y_parent_value) = depthAndParentValue(root, y, 0, 0)

        return x_depth == y_depth and x_parent_value != y_parent_value


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Input: root = [1,2,3,None,4,None,5], x = 5, y = 4
# Output: true
#
# Input: root = [1,2,3,None,4], x = 2, y = 3
# Output: false


def test():
    def case(tree, x: int, y: int, expected: bool) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().isCousins(root, x, y) == expected

    assert case([1, 2, 3, 4], 4, 3, False)
    assert case([1, 2, 3, None, 4, None, 5], 5, 4, True)
    assert case([1, 2, 3, None, 4], 2, 3, False)
