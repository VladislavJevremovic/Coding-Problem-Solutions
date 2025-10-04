# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        """DFS matching arr against root-to-leaf paths, pruning on first mismatch."""

        # Time: O(n)   Space: O(h)
        def dfs(node: TreeNode, arr: List[int], i: int) -> bool:
            if not node or i >= len(arr):
                return False

            if node.val != arr[i]:
                return False

            if (not node.left and not node.right) and i + 1 == len(arr):  # leaf?
                return True
            else:
                return dfs(node.left, arr, i + 1) or dfs(node.right, arr, i + 1)

        return dfs(root, arr, 0)


# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0
# Example 2:
#
#
#
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
# Example 3:
#
#
#
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,1]
# Output: false


def test():
    # The tree [0,1,0,0,1,0,None,None,1,0,0] contains 0 values, which the
    # level-order helper treats as gaps, so build it explicitly here.
    #             A:0
    #          /       \
    #        B:1        C:0
    #       /   \       /
    #     D:0   E:1    F:0
    #       \   /  \
    #      G:1 H:0  I:0
    A = TreeNode(0)
    B = TreeNode(1)
    C = TreeNode(0)
    D = TreeNode(0)
    E = TreeNode(1)
    F = TreeNode(0)
    G = TreeNode(1)
    H = TreeNode(0)
    I = TreeNode(0)
    A.left, A.right = B, C
    B.left, B.right = D, E
    C.left = F
    D.right = G
    E.left, E.right = H, I
    root = A

    def case(arr: List[int], expected: bool) -> bool:
        return Solution().isValidSequence(root, arr) == expected

    assert case([0, 1, 0, 1], True)
    assert case([0, 0, 1], False)
    assert case([0, 1, 1], False)
