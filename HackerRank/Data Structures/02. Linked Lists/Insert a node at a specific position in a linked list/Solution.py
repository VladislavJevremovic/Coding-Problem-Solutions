# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# HackerRank: Insert a node at a specific position in a linked list
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def insert_node_at_position(
    head: Optional[ListNode], data: int, position: int
) -> ListNode:
    """Advance to the node before the target index and splice the new node in."""
    # Time: O(position)   Space: O(1)
    if head is None:
        return ListNode(data)
    if position == 0:
        return ListNode(data, head)
    prev = head
    for _ in range(position - 1):
        assert prev.next is not None
        prev = prev.next
    prev.next = ListNode(data, prev.next)
    return head


def _build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def _to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def test() -> None:
    assert _to_list(insert_node_at_position(_build([1, 2, 3]), 9, 1)) == [1, 9, 2, 3]
    assert _to_list(insert_node_at_position(_build([1, 2, 3]), 9, 0)) == [9, 1, 2, 3]
    assert _to_list(insert_node_at_position(_build([1, 2, 3]), 9, 3)) == [1, 2, 3, 9]
    assert _to_list(insert_node_at_position(None, 9, 0)) == [9]
