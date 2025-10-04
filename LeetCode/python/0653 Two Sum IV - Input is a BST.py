# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import List, Optional

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """DFS the tree keeping a seen-set; return True once the complement of
        any visited value has already been recorded."""

        # Time: O(n)   Space: O(n)
        def dfs(root: Optional[TreeNode], k: int, d: List[int]):
            if not root:
                return False

            if (k - root.val) in d:
                return True

            d.append(root.val)

            return dfs(root.left, k, d) or dfs(root.right, k, d)

        return dfs(root, k, [])


# Input: root = [5,3,6,2,4,None,7], k = 9
# Output: true
# Example 2:
#
#
# Input: root = [5,3,6,2,4,None,7], k = 28
# Output: false
# Example 3:
#
# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:
#
# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:
#
# Input: root = [2,1,3], k = 3
# Output: true


def test():
    def case(tree, k, expected):
        root = BinarySearchTree.from_level_order_sequence(tree).root
        assert Solution().findTarget(root, k) == expected

    case([5, 3, 6, 2, 4, None, 7], 9, True)
    case([5, 3, 6, 2, 4, None, 7], 28, False)
    case([2, 1, 3], 4, True)
    case([2, 1, 3], 1, False)
    case([2, 1, 3], 3, True)
