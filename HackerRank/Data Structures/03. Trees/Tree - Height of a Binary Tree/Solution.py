# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# HackerRank: Tree - Height of a Binary Tree
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


def height(root: Optional[Node]) -> int:
    """Recursively return 1 + the taller subtree's height (edges); empty tree is -1."""
    # Time: O(n)   Space: O(h)  (recursion depth; h = tree height)
    # Height measured in edges: empty tree is -1, single node is 0.
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


def test() -> None:
    assert height(None) == -1
    assert height(Node(1)) == 0
    #        1
    #       / \
    #      2   5
    #     / \
    #    3   4
    root = Node(1, Node(2, Node(3), Node(4)), Node(5))
    assert height(root) == 2
    # Degenerate (linked-list-like) tree of 4 nodes -> height 3
    deep = Node(1, Node(2, Node(3, Node(4))))
    assert height(deep) == 3
