# https://leetcode.com/problems/merge-two-binary-trees/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """Recursively overlay the trees, summing values where both nodes exist
        and reusing the lone subtree where only one does."""
        # Time: O(min(m, n))   Space: O(min(m, n))   (recursion stack)
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            tmp = TreeNode(t1.val + t2.val)
            tmp.left = self.mergeTrees(t1.left, t2.left)
            tmp.right = self.mergeTrees(t1.right, t2.right)

            return tmp


# Input: root1 = [1,3,2,5], root2 = [2,1,3,None,4,None,7]
# Output: [3,4,5,5,4,None,7]
# Example 2:
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]


def test():
    def case(t1_tree, t2_tree, expected) -> bool:
        t1 = (
            BinarySearchTree.from_level_order_sequence(t1_tree).root
            if t1_tree
            else None
        )
        t2 = (
            BinarySearchTree.from_level_order_sequence(t2_tree).root
            if t2_tree
            else None
        )
        result = Solution().mergeTrees(t1, t2)
        return BinarySearchTree(result).to_level_order() == expected

    assert case([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7])
    assert case([1], [1, 2], [2, 2])
