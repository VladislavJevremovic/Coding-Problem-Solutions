from typing import Optional, List, Generic, TypeVar

T = TypeVar("T")


class SinglyLinkedNode(Generic[T]):
    def __init__(self, val: T, next: Optional['SinglyLinkedNode'] = None):
        self.val = val
        self.next = next


class SinglyLinkedList(Generic[T]):
    def __init__(self, head: Optional[SinglyLinkedNode] = None):
        self.head = head

    def __eq__(self, other):
        if isinstance(other, SinglyLinkedList):
            return self.to_list() == other.to_list()

        return NotImplemented

    @classmethod
    def from_sequence(cls, sequence: Optional[T]) -> 'SinglyLinkedList':
        linked_list = cls()
        if sequence:
            for val in reversed(sequence):
                linked_list.head = SinglyLinkedNode(val, linked_list.head)

        return linked_list

    def to_list(self) -> List[T]:
        result = []
        t = self.head
        while t and isinstance(t, SinglyLinkedNode):
            result.append(t.val)
            t = t.next

        return result
