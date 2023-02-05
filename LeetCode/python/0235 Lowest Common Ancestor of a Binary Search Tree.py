# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from typing import Optional

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
