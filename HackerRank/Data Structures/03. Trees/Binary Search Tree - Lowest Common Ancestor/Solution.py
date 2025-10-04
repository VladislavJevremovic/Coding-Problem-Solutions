# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
# HackerRank: Binary Search Tree - Lowest Common Ancestor
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


def lca(root: Optional[Node], v1: int, v2: int) -> Optional[Node]:
    """Descend the BST until the split point where v1 and v2 diverge - that node is the LCA."""
    # Time: O(h)   Space: O(1)  (h = tree height)
    node = root
    while node is not None:
        if node.val > v1 and node.val > v2:
            node = node.left
        elif node.val < v1 and node.val < v2:
            node = node.right
        else:
            return node
    return None


def test() -> None:
    #            4
    #          /   \
    #         2     6
    #        / \   / \
    #       1   3 5   7
    root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    assert lca(root, 1, 3) is not None and lca(root, 1, 3).val == 2
    assert lca(root, 1, 7) is not None and lca(root, 1, 7).val == 4
    assert lca(root, 5, 7) is not None and lca(root, 5, 7).val == 6
    # One value is an ancestor of the other
    assert lca(root, 2, 3) is not None and lca(root, 2, 3).val == 2
    # Order of arguments should not matter
    assert lca(root, 7, 1).val == 4
