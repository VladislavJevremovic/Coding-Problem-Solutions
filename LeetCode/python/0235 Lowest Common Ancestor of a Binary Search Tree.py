# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from typing import Optional

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        """Walk down recursively: if both targets are below root go that way,
        otherwise the split point (or a matched node) is the LCA."""
        # Time: O(h)   Space: O(h)
        if not root:
            return None

        a, b = min(p.val, q.val), max(p.val, q.val)
        if root.val < a:
            return self.lowestCommonAncestor(root.right, p, q)
        elif b < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


class Solution2:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """Same BST descent, iterated with a loop instead of recursion."""
        # Time: O(h)   Space: O(1)
        a, b = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < a:
                root = root.right
            elif b < root.val:
                root = root.left
            else:
                return root

        return None


# Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
# Output: 2
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2


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

    def case(tree, p_val, q_val, expected):
        for solution in (Solution(), Solution2()):
            root = BinarySearchTree.from_level_order_sequence(tree).root
            p, q = find(root, p_val), find(root, q_val)
            assert solution.lowestCommonAncestor(root, p, q).val == expected

    case([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6)
    case([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2)
    case([2, 1], 2, 1, 2)
