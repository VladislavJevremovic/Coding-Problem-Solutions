# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
# HackerRank: Reverse a doubly linked list
from typing import Optional


class DoublyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["DoublyLinkedListNode"] = None
        self.prev: Optional["DoublyLinkedListNode"] = None


def reverse(head: Optional[DoublyLinkedListNode]) -> Optional[DoublyLinkedListNode]:
    """Swap each node's prev/next pointers in one pass; the last node becomes the head."""
    # Time: O(n)   Space: O(1)
    node = head
    new_head = head
    while node is not None:
        node.prev, node.next = node.next, node.prev
        new_head = node
        node = node.prev  # this is the original next, after the swap
    return new_head


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
    """Walk to the tail then back via prev, verifying the prev links."""
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
    head = build_list([1, 2, 3, 4])
    reversed_head = reverse(head)
    assert to_list(reversed_head) == [4, 3, 2, 1]
    # prev links must also be consistent (forward via prev from tail back to head)
    assert to_list_reverse(reversed_head) == [1, 2, 3, 4]
    # edge case: single node
    assert to_list(reverse(build_list([7]))) == [7]
    # edge case: empty list
    assert to_list(reverse(None)) == []
