# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
# HackerRank: Binary Search Tree - Insertion
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


def insert(root: Optional[Node], data: int) -> Node:
    """Recursively descend left/right by BST ordering and attach a new leaf."""
    # Time: O(h)   Space: O(h)  (recursion depth; h = tree height)
    if root is None:
        return Node(data)
    if data < root.val:
        root.left = insert(root.left, data)
    elif data > root.val:
        root.right = insert(root.right, data)
    return root


def _in_order(root: Optional[Node]) -> List[int]:
    if root is None:
        return []
    return _in_order(root.left) + [root.val] + _in_order(root.right)


def test() -> None:
    root: Optional[Node] = None
    for v in [4, 2, 3, 1, 7, 6]:
        root = insert(root, v)
    # In-order traversal of a BST is sorted
    assert _in_order(root) == [1, 2, 3, 4, 6, 7]
    assert root is not None and root.val == 4
    assert root.left is not None and root.left.val == 2
    assert root.right is not None and root.right.val == 7
    # Duplicate value should not change the tree
    before = _in_order(root)
    root = insert(root, 4)
    assert _in_order(root) == before
