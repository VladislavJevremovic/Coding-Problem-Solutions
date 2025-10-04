# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# HackerRank: Tree - Level Order Traversal
from collections import deque
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def level_order(root: Optional[Node]) -> list[int]:
    """BFS with a queue, enqueuing children left-to-right to emit nodes level by level."""
    # Time: O(n)   Space: O(n)  (queue + output)
    result: list[int] = []
    if root is None:
        return result
    queue: deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def insert(root: Optional[Node], data: int) -> Node:
    """Insert into a binary search tree (used to build test fixtures)."""
    if root is None:
        return Node(data)
    if data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def test() -> None:
    #        3
    #       / \
    #      2   5
    #     /   / \
    #    1   4   6
    root: Optional[Node] = None
    for value in [3, 2, 5, 1, 4, 6]:
        root = insert(root, value)
    assert level_order(root) == [3, 2, 5, 1, 4, 6]
    # edge case: empty tree
    assert level_order(None) == []
    # edge case: single node
    assert level_order(Node(42)) == [42]
