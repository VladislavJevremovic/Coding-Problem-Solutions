# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution1:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            r = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    r.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            r = r[::-1] if len(result) % 2 else r
            if r:
                result.append(r)

        return result


class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        Q = [root]
        right_start = 0
        if root:
            while Q:
                n = len(Q)
                levels.append([])
                for i in range(n):
                    cur = Q.pop(0)
                    if cur.left:
                        Q.append(cur.left)
                    if cur.right:
                        Q.append(cur.right)
                    levels[-1].append(cur.val)
                if right_start & 1:
                    levels[-1] = levels[-1][::-1]
                right_start ^= 1

        return levels


def test():
    def case(list1: List[int], expected: List[List[int]]) -> bool:
        tree = BinarySearchTree.from_level_order_sequence(list1)
        return Solution1().zigzagLevelOrder(tree.root) == expected if tree else not expected

    assert case([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]])
    assert case([1], [[1]])
    assert case([], [])
