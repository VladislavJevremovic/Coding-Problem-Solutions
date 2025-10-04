# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """Recursive postorder (left, right, node) built by list concatenation."""
        # Time: O(n^2)   Space: O(n)  (list concat at each node)
        if not root:
            return []

        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """Iterative traversal that visits node-right-left and prepends each
        value, producing left-right-node order."""
        # Time: O(n^2)   Space: O(n)  (insert(0, ...) is O(n) each)
        result = []

        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.insert(0, node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result


# Input: root = [1,None,2,3]
# Output: [3,2,1]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
# Example 5:
#
#
# Input: root = [1,None,2]
# Output: [2,1]


def test():
    def case(tree, expected: List[int]) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return (
            Solution1().postorderTraversal(root) == expected
            and Solution2().postorderTraversal(root) == expected
        )

    assert case([1, None, 2, 3], [3, 2, 1])
    assert case([], [])
    assert case([1], [1])
    assert case([1, 2], [2, 1])
