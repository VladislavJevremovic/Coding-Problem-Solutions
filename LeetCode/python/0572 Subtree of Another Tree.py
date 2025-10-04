# https://leetcode.com/problems/subtree-of-another-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        """Structurally compare two trees node by node for exact equality."""
        # Time: O(min(m, n))   Space: O(min(m, n))   (recursion stack)
        if not s and not t:
            return True
        if not s or not t:
            return False

        return (
            s.val == t.val
            and self.isSameTree(s.left, t.left)
            and self.isSameTree(s.right, t.right)
        )

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """At every node of s, test whether the subtree rooted there equals t."""
        # Time: O(m * n)   Space: O(h)   (recursion stack; h = height of s)
        if not s:
            return False
        if not t:
            return True

        return (
            self.isSameTree(s, t)
            or self.isSubtree(s.left, t)
            or self.isSubtree(s.right, t)
        )


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#
#
# Input: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
# Output: false


def test():
    def case(s_tree, t_tree, expected: bool) -> bool:
        s = BinarySearchTree.from_level_order_sequence(s_tree).root if s_tree else None
        t = BinarySearchTree.from_level_order_sequence(t_tree).root if t_tree else None
        return Solution().isSubtree(s, t) == expected

    assert case([3, 4, 5, 1, 2], [4, 1, 2], True)
    assert case([3, 4, 5, 1, 2, None, None, None, None, 6], [4, 1, 2], False)
