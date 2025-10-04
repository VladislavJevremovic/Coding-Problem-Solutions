# https://www.hackerrank.com/challenges/tree-top-view/problem
# HackerRank: Tree - Top View

from queue import Queue
from typing import List, Optional


class Node:
    def __init__(self, info: int) -> None:
        self.info = info
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.level: Optional[int] = None


def topView(root: Optional[Node]) -> List[int]:
    """BFS tagging each node with a horizontal level; first node seen per level is visible."""
    # Time: O(n log n)   Space: O(n)  (sorting the level->value map by column)
    q: "Queue[Node]" = Queue()
    m: dict = {}

    if root:
        root.level = 0
        q.put(root)

    while not q.empty():
        n = q.get()

        level = n.level
        if level not in m:
            m[level] = n.info

        if n.left:
            n.left.level = level - 1
            q.put(n.left)
        if n.right:
            n.right.level = level + 1
            q.put(n.right)

    return [m[k] for k in sorted(m)]


def _insert(root, value):
    # Binary search tree insertion (HackerRank builds the tree this way).
    if root is None:
        return Node(value)
    if value <= root.info:
        root.left = _insert(root.left, value)
    else:
        root.right = _insert(root.right, value)
    return root


def _build_bst(values):
    root = None
    for v in values:
        root = _insert(root, v)
    return root


def test():
    # Empty tree has no top view.
    assert topView(None) == []

    # Single node.
    assert topView(Node(5)) == [5]

    #        1
    #         \
    #          2
    #           \
    #            5
    #           / \
    #          3   6
    #           \
    #            4
    # Built as a BST from this insertion order.
    root = _build_bst([1, 2, 5, 3, 6, 4])
    # Horizontal distances: 1->0, 2->1, 5->2, 3->1(taken first by 2), 6->3, 4->2(taken by 5)
    # Top view by column: 1(0), 2(1), 5(2), 6(3)
    assert topView(root) == [1, 2, 5, 6]

    # Balanced-ish tree where left subtree contributes leftmost columns.
    #          4
    #        /   \
    #       2     6
    #      / \   / \
    #     1   3 5   7
    balanced = _build_bst([4, 2, 6, 1, 3, 5, 7])
    assert topView(balanced) == [1, 2, 4, 6, 7]
