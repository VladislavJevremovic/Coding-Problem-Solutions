"""Doubly linked list node and list with sentinel head/tail for O(1) edits."""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class DoublyLinkedNode(Generic[T]):
    """A node holding key/value plus links to its previous and next nodes."""

    def __init__(
        self,
        key: Optional[T] = None,
        value: Optional[T] = None,
        prev: Optional["DoublyLinkedNode"] = None,
        next: Optional["DoublyLinkedNode"] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList(Generic[T]):
    """Doubly linked list bounded by sentinel head and tail nodes."""

    def __init__(self, default: Optional[T] = None):
        self.head = DoublyLinkedNode(value=default)
        self.tail = DoublyLinkedNode(value=default)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_head(self, node: DoublyLinkedNode):
        """Insert an existing node right after the head sentinel."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def add_node_to_tail(self, node: DoublyLinkedNode):
        """Insert an existing node right before the tail sentinel."""
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def remove_node(self, node: DoublyLinkedNode):
        """Unlink a node by joining its neighbours together."""
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

    def move_node_to_head(self, node: DoublyLinkedNode):
        """Move an existing node to the front of the list."""
        self.remove_node(node)
        self.add_node_to_head(node)

    def add_value_to_tail(self, value: T) -> DoublyLinkedNode:
        """Wrap a value in a new node, append it before the tail, and return it."""
        new_node = DoublyLinkedNode(value=value)
        self.add_node_to_tail(new_node)

        return new_node

    def pop_tail(self):
        """Remove and return the last real node (before the tail sentinel)."""
        res = self.tail.prev
        self.remove_node(res)

        return res

    def first_value(self) -> Optional[T]:
        """Return the value of the first real node, or None if empty."""
        if self.is_empty():
            return None

        return self.head.next.value

    def is_empty(self):
        """Return True when only the head and tail sentinels remain."""
        return self.head.next is self.tail
