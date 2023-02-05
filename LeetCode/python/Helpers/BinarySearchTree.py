from collections import deque
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class BinarySearchNode(Generic[T]):
    def __init__(self, val: T, left: Optional['BinarySearchNode'] = None, right: Optional['BinarySearchNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(Generic[T]):
    def __init__(self, root: Optional[BinarySearchNode] = None):
        self.root = root

    def __eq__(self, other):
        if isinstance(other, BinarySearchTree):
            return self.in_order() == other.in_order()

        return NotImplemented

    def in_order(self, root) -> [T]:
        return self.in_order(root.left) + [root.val] + self.in_order(root.right) if root else []

    @classmethod
    def from_sequence(cls, sequence: Optional[T]) -> Optional['BinarySearchTree']:
        if not sequence:
            return None

        nodes = [None if not val else BinarySearchNode(val) for val in sequence]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()

        return cls(root)

    @classmethod
    def from_level_order_sequence(cls, sequence: Optional[T]) -> Optional['BinarySearchTree']:
        if not sequence:
            return None

        root = BinarySearchNode(sequence[0])
        q = deque([root])
        i = 1
        while q and i < len(sequence):
            node = q.popleft()

            if sequence[i]:
                node.left = BinarySearchNode(sequence[i])
                q.append(node.left)
            i += 1
            if i < len(sequence):
                if sequence[i]:
                    node.right = BinarySearchNode(sequence[i])
                    q.append(node.right)
                i += 1

        return cls(root)
