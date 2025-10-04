# https://www.hackerrank.com/challenges/is-this-a-binary-search-tree/problem
# HackerRank: Is This a Binary Search Tree
from typing import Optional


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


def check_bst(root: Optional[Node]) -> bool:
    """Recursively verify every node lies within the (low, high) bound its position allows."""

    # Time: O(n)   Space: O(h)  (recursion depth; h = tree height)
    def values_in_range(node: Optional[Node], low: int, high: int) -> bool:
        if node is None:
            return True
        if node.val < low or node.val > high:
            return False
        return values_in_range(node.left, low, node.val - 1) and values_in_range(
            node.right, node.val + 1, high
        )

    return values_in_range(root, float("-inf"), float("inf"))


def test() -> None:
    # Valid BST
    valid = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    assert check_bst(valid) is True
    # Invalid: 5 is in the left subtree of 4 but greater than 4
    invalid = Node(4, Node(2, Node(1), Node(5)), Node(6))
    assert check_bst(invalid) is False
    # Duplicate values make it invalid (strict BST)
    dup = Node(2, Node(2), Node(3))
    assert check_bst(dup) is False
    assert check_bst(None) is True
    assert check_bst(Node(1)) is True
