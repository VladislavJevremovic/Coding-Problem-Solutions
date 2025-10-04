# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Pick the middle element as the root and recurse on the two halves;
        slicing copies each half."""
        # Time: O(n log n)   Space: O(n)  (slice copies at each level)
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Build the balanced BST with index bounds instead of slicing, so each
        element is visited once."""

        # Time: O(n)   Space: O(log n)
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)

            return root

        return helper(0, len(nums) - 1)


# def test():
#     def case(list1: List[int], expected: List[int]) -> bool:
#         tree = BinarySearchTree.from_level_order_sequence(list1)
#         return Solution().levelOrder(tree.root) == expected if tree else not expected
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,None,5]
# Explanation: [0,-10,5,None,-3,None,9] is also accepted:
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
