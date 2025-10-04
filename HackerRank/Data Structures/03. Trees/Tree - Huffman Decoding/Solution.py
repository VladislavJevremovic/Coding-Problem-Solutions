# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
# HackerRank: Tree - Huffman Decoding
from typing import Optional


class Node:
    def __init__(
        self,
        char: Optional[str] = None,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
    ) -> None:
        # Leaf nodes carry a character; internal nodes have char == None.
        self.char = char
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


def decode_huff(root: Node, encoded: str) -> str:
    """Walk the Huffman tree bit by bit, emitting a character and resetting to root at each leaf."""
    # Time: O(len(encoded))   Space: O(len(decoded))  (output buffer)
    decoded = []
    node = root
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        assert node is not None
        if node.is_leaf():
            decoded.append(node.char)
            node = root
    return "".join(decoded)


def test() -> None:
    # Build a Huffman tree for: A=0, B=10, C=11
    #          *
    #         / \
    #        A   *
    #           / \
    #          B   C
    root = Node(
        left=Node(char="A"),
        right=Node(left=Node(char="B"), right=Node(char="C")),
    )
    # ABACA -> 0 10 0 11 0
    assert decode_huff(root, "010011" + "0") == "ABACA"
    assert decode_huff(root, "0") == "A"
    assert decode_huff(root, "1011") == "BC"
    assert decode_huff(root, "") == ""
