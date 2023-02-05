# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return []

            return dfs(node.left) + [node.val] + dfs(node.right)

        return dfs(root)[k - 1]


class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            k -= 1
            if not k:
                return root.val

            root = root.right

# def test():
#     s = Solution2()
#     assert s.kthSmallest([3, 1, 4, None, 2], 1) == 1
#     assert s.kthSmallest([5, 3, 6, 2, 4, None, None, 1], 3) == 3
