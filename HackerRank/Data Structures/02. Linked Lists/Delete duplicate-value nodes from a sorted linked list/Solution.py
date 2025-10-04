# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
# HackerRank: Delete duplicate-value nodes from a sorted linked list
from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["SinglyLinkedListNode"] = None


def remove_duplicates(
    head: Optional[SinglyLinkedListNode],
) -> Optional[SinglyLinkedListNode]:
    """Single pass over the sorted list, unlinking each node equal to its predecessor."""
    # Time: O(n)   Space: O(1)
    node = head
    while node is not None and node.next is not None:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head


def build_list(values: list[int]) -> Optional[SinglyLinkedListNode]:
    head: Optional[SinglyLinkedListNode] = None
    tail: Optional[SinglyLinkedListNode] = None
    for value in values:
        node = SinglyLinkedListNode(value)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[SinglyLinkedListNode]) -> list[int]:
    result: list[int] = []
    node = head
    while node is not None:
        result.append(node.data)
        node = node.next
    return result


def test() -> None:
    assert to_list(remove_duplicates(build_list([1, 2, 2, 3, 3, 4]))) == [1, 2, 3, 4]
    # consecutive run of duplicates
    assert to_list(remove_duplicates(build_list([1, 1, 1, 1]))) == [1]
    # no duplicates
    assert to_list(remove_duplicates(build_list([1, 2, 3]))) == [1, 2, 3]
    # edge case: empty list
    assert to_list(remove_duplicates(None)) == []
