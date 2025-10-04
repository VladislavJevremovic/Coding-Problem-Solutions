"""Binary tree node and tree wrapper with level-order (de)serialization."""

from collections import deque
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class BinarySearchNode(Generic[T]):
    """A binary tree node holding a value and left/right child links."""

    def __init__(
        self,
        val: T,
        left: Optional["BinarySearchNode"] = None,
        right: Optional["BinarySearchNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(Generic[T]):
    """Wrapper around a root node, comparable by level-order structure."""

    def __init__(self, root: Optional[BinarySearchNode] = None):
        self.root = root

    def __eq__(self, other):
        if isinstance(other, BinarySearchTree):
            # Compare by structure (level-order), not just values, so that two
            # differently shaped trees holding the same values are not equal.
            return self.to_level_order() == other.to_level_order()

        return NotImplemented

    _UNSET = object()

    def in_order(self, root=_UNSET) -> List[T]:
        """Return node values via an in-order (left, root, right) traversal."""
        if root is BinarySearchTree._UNSET:
            root = self.root
        return (
            self.in_order(root.left) + [root.val] + self.in_order(root.right)
            if root
            else []
        )

    def to_level_order(self) -> List[Optional[T]]:
        """Serialize to a LeetCode-style level-order list with trailing Nones trimmed."""
        result = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    @classmethod
    def from_sequence(cls, sequence: Optional[T]) -> Optional["BinarySearchTree"]:
        """Build a tree by assigning children left-to-right from the sequence."""
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
    def from_level_order_sequence(
        cls, sequence: Optional[T]
    ) -> Optional["BinarySearchTree"]:
        """Build a tree from a LeetCode-style level-order list (None marks gaps)."""
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
