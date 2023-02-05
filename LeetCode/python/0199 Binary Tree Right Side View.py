# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
