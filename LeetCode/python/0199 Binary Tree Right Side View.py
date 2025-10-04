# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque
from typing import List, Optional

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS level by level, recording the last node visited on each level as
        the value seen from the right side."""
        # Time: O(n)   Space: O(n)
        if not root:
            return []

        queue = deque([root])
        right_side = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    right_side.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side


# Input: root = [1,2,3,None,5,None,4]
# Output: [1,3,4]
# Example 2:
#
# Input: root = [1,None,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []


def test():
    def case(tree, expected: List[int]) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().rightSideView(root) == expected

    assert case([1, 2, 3, None, 5, None, 4], [1, 3, 4])
    assert case([1, None, 3], [1, 3])
    assert case([], [])
