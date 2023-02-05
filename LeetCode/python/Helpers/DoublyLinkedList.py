from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class DoublyLinkedNode(Generic[T]):
    def __init__(
            self,
            key: Optional[T] = None,
            value: Optional[T] = None,
            prev: Optional['DoublyLinkedNode'] = None,
            next: Optional['DoublyLinkedNode'] = None
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList(Generic[T]):
    def __init__(self, default: Optional[T] = None):
        self.head = DoublyLinkedNode(value=default)
        self.tail = DoublyLinkedNode(value=default)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_head(self, node: DoublyLinkedNode):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def add_node_to_tail(self, node: DoublyLinkedNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def remove_node(self, node: DoublyLinkedNode):
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

    def move_node_to_head(self, node: DoublyLinkedNode):
        self.remove_node(node)
        self.add_node_to_head(node)

    def add_value_to_tail(self, value: T) -> DoublyLinkedNode:
        new_node = DoublyLinkedNode(value)
        self.add_node_to_tail(new_node)

        return new_node

    def pop_tail(self):
        res = self.tail.prev
        self.remove_node(res)

        return res

    def first_value(self) -> Optional[T]:
        if self.is_empty():
            return None

        return self.head.next.value

    def is_empty(self):
        return self.head.next is self.tail
