# https://leetcode.com/problems/path-sum/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """Recurse down, subtracting each node's value from the target, and
        check the remainder at the leaves."""
        # Time: O(n)   Space: O(h)
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right


# Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
# Output: true
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: false


def test():
    def case(tree, target: int, expected: bool) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().hasPathSum(root, target) == expected

    assert case([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
    assert case([1, 2, 3], 5, False)
    assert case([1, 2], 0, False)
    assert case([], 0, False)
