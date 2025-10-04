# https://www.hackerrank.com/challenges/inserting-a-node-into-a-sorted-doubly-linked-list/problem
# HackerRank: Inserting a Node Into a Sorted Doubly Linked List
from typing import Optional


class DoublyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["DoublyLinkedListNode"] = None
        self.prev: Optional["DoublyLinkedListNode"] = None


def sorted_insert(
    head: Optional[DoublyLinkedListNode], data: int
) -> Optional[DoublyLinkedListNode]:
    """Scan to the correct sorted position and relink prev/next pointers around the new node."""
    # Time: O(n)   Space: O(1)
    new_node = DoublyLinkedListNode(data)
    if head is None:
        return new_node

    # Insert before head.
    if data <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    # Find the last node whose data is <= data.
    node = head
    while node.next is not None and node.next.data < data:
        node = node.next

    new_node.next = node.next
    new_node.prev = node
    if node.next is not None:
        node.next.prev = new_node
    node.next = new_node
    return head


def build_list(values: list[int]) -> Optional[DoublyLinkedListNode]:
    head: Optional[DoublyLinkedListNode] = None
    tail: Optional[DoublyLinkedListNode] = None
    for value in values:
        node = DoublyLinkedListNode(value)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            node.prev = tail
            tail = node
    return head


def to_list(head: Optional[DoublyLinkedListNode]) -> list[int]:
    result: list[int] = []
    node = head
    while node is not None:
        result.append(node.data)
        node = node.next
    return result


def to_list_reverse(head: Optional[DoublyLinkedListNode]) -> list[int]:
    result: list[int] = []
    node = head
    prev = None
    while node is not None:
        prev = node
        node = node.next
    while prev is not None:
        result.append(prev.data)
        prev = prev.prev
    return result


def test() -> None:
    # insert in the middle
    head = sorted_insert(build_list([1, 3, 4, 10]), 5)
    assert to_list(head) == [1, 3, 4, 5, 10]
    # prev links are consistent: walking from tail back gives reverse order
    assert to_list_reverse(head) == [10, 5, 4, 3, 1]
    # insert at the front
    assert to_list(sorted_insert(build_list([2, 3, 4]), 1)) == [1, 2, 3, 4]
    # insert at the end
    assert to_list(sorted_insert(build_list([1, 2, 3]), 9)) == [1, 2, 3, 9]
    # edge case: empty list
    assert to_list(sorted_insert(None, 5)) == [5]
