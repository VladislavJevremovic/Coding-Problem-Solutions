# https://leetcode.com/problems/path-sum-ii/

from typing import List, Optional

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """Backtrack down every root-to-leaf path, recording a copy of the path
        whenever its values sum to the target."""

        # Time: O(n^2)   Space: O(n)  (path copy can be O(n) per leaf)
        def backtrack(node, remainder, current_path, result):
            if not node:
                return

            current_path.append(node.val)
            if remainder == node.val and not node.left and not node.right:
                result.append(current_path[:])
            else:
                backtrack(node.left, remainder - node.val, current_path, result)
                backtrack(node.right, remainder - node.val, current_path, result)

            current_path.pop()

        result = []
        backtrack(root, targetSum, [], result)

        return result


# Input: root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Input: root = [1,2], targetSum = 0
# Output: []


def test():
    def case(tree, target: int, expected: List[List[int]]) -> bool:
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        return Solution().pathSum(root, target) == expected

    assert case(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
        22,
        [[5, 4, 11, 2], [5, 8, 4, 5]],
    )
    assert case([1, 2, 3], 5, [])
    assert case([1, 2], 0, [])
    assert case([], 0, [])
