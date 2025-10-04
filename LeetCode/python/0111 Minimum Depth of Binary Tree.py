# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """Recurse for the shortest root-to-leaf depth, treating a missing
        child as infinite so single-child nodes don't count as leaves."""
        # Time: O(n)   Space: O(h)
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_depth = (1 + self.minDepth(root.left)) if root.left else float("inf")
        right_depth = (1 + self.minDepth(root.right)) if root.right else float("inf")

        return min(left_depth, right_depth)


# Input: root = [3,9,20,None,None,15,7]
# Output: 2
#
# Input: root = [2,None,3,None,4,None,5,None,6]
# Output: 5


def test():
    def case(tree, expected: int) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().minDepth(root) == expected

    assert case([3, 9, 20, None, None, 15, 7], 2)
    assert case([2, None, 3, None, 4, None, 5, None, 6], 5)
    assert case([], 0)
    assert case([1], 1)
