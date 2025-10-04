# https://leetcode.com/problems/search-in-a-binary-search-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """Recurse into both subtrees and return the first node matching the
        value (does not exploit BST ordering)."""
        # Time: O(n)   Space: O(h)
        if not root:
            return None

        if root.val == val:
            return root

        return self.searchBST(root.left, val) or self.searchBST(root.right, val)


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []


def test():
    def case(tree, val: int, expected) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        result = Solution().searchBST(root, val)
        return BinarySearchTree(result).to_level_order() == expected

    assert case([4, 2, 7, 1, 3], 2, [2, 1, 3])
    assert case([4, 2, 7, 1, 3], 5, [])
