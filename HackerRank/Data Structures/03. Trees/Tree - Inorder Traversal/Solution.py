# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
# HackerRank: Tree - Inorder Traversal
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


def in_order(root: Optional[Node]) -> List[int]:
    """Recursively concatenate left subtree, this node, then right subtree."""
    # Time: O(n^2) worst / O(n log n) balanced (list concatenation)   Space: O(n)
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


def test() -> None:
    #        1
    #       / \
    #      2   5
    #     / \
    #    3   4
    root = Node(1, Node(2, Node(3), Node(4)), Node(5))
    assert in_order(root) == [3, 2, 4, 1, 5]
    assert in_order(None) == []
    # A BST in-order traversal is sorted
    bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    assert in_order(bst) == [1, 2, 3, 4, 5, 6, 7]
