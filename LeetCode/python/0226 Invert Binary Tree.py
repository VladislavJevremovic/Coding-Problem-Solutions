# https://leetcode.com/problems/invert-binary-tree/

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Recursively invert both subtrees, then swap them at the current node."""
        # Time: O(n)   Space: O(h)
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Iteratively traverse with a stack/queue, swapping each node's children
        as it is visited."""
        # Time: O(n)   Space: O(n)
        if not root:
            return root

        queue = [root]
        while queue:
            current = queue.pop()
            temp = current.left
            current.left = current.right
            current.right = temp

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
# Input: root = []
# Output: []


def test():
    def case(tree, expected) -> bool:
        for Solution in (Solution1, Solution2):
            root = (
                BinarySearchTree.from_level_order_sequence(tree).root if tree else None
            )
            result = Solution().invertTree(root)
            if BinarySearchTree(result).to_level_order() != expected:
                return False
        return True

    assert case([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])
    assert case([2, 1, 3], [2, 3, 1])
    assert case([], [])
