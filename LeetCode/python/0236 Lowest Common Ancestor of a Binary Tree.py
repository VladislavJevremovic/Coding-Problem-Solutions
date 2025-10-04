# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """Post-order DFS returning whether p or q is in each subtree; the node
        where two of {self-match, left, right} are true is the LCA."""

        # Time: O(n)   Space: O(h)
        def recurse_tree(current_node) -> bool:
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            current = current_node in (p, q)

            # if two of three True, found it
            if current + left + right >= 2:
                self.result = current_node

            return current or left or right

        recurse_tree(root)

        return self.result


# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
# Output: 3
#
# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
# Output: 5
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1


def test():
    def find(root, val):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                stack.append(node.left)
                stack.append(node.right)
        return None

    def case(tree, p_val, q_val, expected):
        root = BinarySearchTree.from_level_order_sequence(tree).root
        p, q = find(root, p_val), find(root, q_val)
        assert Solution().lowestCommonAncestor(root, p, q).val == expected

    case([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3)
    case([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5)
    case([1, 2], 1, 2, 1)
