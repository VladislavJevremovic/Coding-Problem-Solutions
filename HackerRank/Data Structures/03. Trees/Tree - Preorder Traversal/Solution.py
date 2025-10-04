# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
# HackerRank: Tree - Preorder Traversal
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def pre_order(root: Optional[Node]) -> List[int]:
    """Recursively concatenate this node, left subtree, then right subtree."""
    # Time: O(n^2) worst / O(n log n) balanced (list concatenation)   Space: O(n)
    if root is None:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)


def test() -> None:
    #        1
    #       / \
    #      2   5
    #     / \
    #    3   4
    root = Node(1, Node(2, Node(3), Node(4)), Node(5))
    assert pre_order(root) == [1, 2, 3, 4, 5]
    assert pre_order(None) == []
    bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    assert pre_order(bst) == [4, 2, 1, 3, 6, 5, 7]
