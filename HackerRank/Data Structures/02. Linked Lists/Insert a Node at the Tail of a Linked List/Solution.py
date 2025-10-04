# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# HackerRank: Insert a Node at the Tail of a Linked List
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def insert_node_at_tail(head: Optional[ListNode], data: int) -> ListNode:
    """Walk to the last node and link the new node after it (or return it if empty)."""
    # Time: O(n)   Space: O(1)
    new_node = ListNode(data)
    if head is None:
        return new_node
    seeker = head
    while seeker.next is not None:
        seeker = seeker.next
    seeker.next = new_node
    return head


def _to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def test() -> None:
    head: Optional[ListNode] = None
    for v in [1, 2, 3]:
        head = insert_node_at_tail(head, v)
    assert _to_list(head) == [1, 2, 3]
    head = insert_node_at_tail(head, 4)
    assert _to_list(head) == [1, 2, 3, 4]
    assert _to_list(insert_node_at_tail(None, 9)) == [9]
