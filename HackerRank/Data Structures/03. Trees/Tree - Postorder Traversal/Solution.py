# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
# HackerRank: Tree - Postorder Traversal
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


def post_order(root: Optional[Node]) -> List[int]:
    """Recursively concatenate left subtree, right subtree, then this node."""
    # Time: O(n^2) worst / O(n log n) balanced (list concatenation)   Space: O(n)
    if root is None:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]


def _build_bst(values: List[int]) -> Optional[Node]:
    root: Optional[Node] = None
    for v in values:
        root = _insert(root, v)
    return root


def _insert(root: Optional[Node], v: int) -> Node:
    if root is None:
        return Node(v)
    if v < root.val:
        root.left = _insert(root.left, v)
    else:
        root.right = _insert(root.right, v)
    return root


def test() -> None:
    #        1
    #       / \
    #      2   5
    #     / \
    #    3   4
    root = Node(1, Node(2, Node(3), Node(4)), Node(5))
    assert post_order(root) == [3, 4, 2, 5, 1]
    assert post_order(None) == []
    # BST built from insertions
    bst = _build_bst([4, 2, 6, 1, 3, 5, 7])
    assert post_order(bst) == [1, 3, 2, 5, 7, 6, 4]
