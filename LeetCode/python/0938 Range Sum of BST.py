# https://leetcode.com/problems/range-sum-of-bst/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution1:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """Recursively sum every node whose value falls within [L, R],
        traversing the whole tree."""
        # Time: O(n)   Space: O(h)
        if not root:
            return 0

        sum = 0
        sum += self.rangeSumBST(root.left, L, R)
        if L <= root.val <= R:
            sum += root.val
        sum += self.rangeSumBST(root.right, L, R)

        return sum


class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """Iterative DFS that prunes subtrees out of [L, R] using the BST
        ordering, visiting only relevant nodes."""
        # Time: O(n)   Space: O(h)
        sum = 0

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    sum += node.val

                if node.val > L:
                    stack.append(node.left)

                if node.val < R:
                    stack.append(node.right)

        return sum


def test():
    def case(tree: List[int], L: int, R: int, expected: int) -> bool:
        return (
            Solution2().rangeSumBST(
                BinarySearchTree.from_level_order_sequence(tree).root, L, R
            )
            == expected
        )

    assert case([10, 5, 15, 3, 7, None, 18], 7, 15, 32)
    assert case([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23)
