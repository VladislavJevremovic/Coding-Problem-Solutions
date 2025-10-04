# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# HackerRank: Insert a node at the head of a linked list
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def insert_node_at_head(head: Optional[ListNode], data: int) -> ListNode:
    """Create a new node pointing at the current head and return it as the new head."""
    # Time: O(1)   Space: O(1)
    return ListNode(data, head)


def _to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def test() -> None:
    head: Optional[ListNode] = None
    for v in [1, 2, 3]:
        head = insert_node_at_head(head, v)
    # Inserting at head reverses insertion order
    assert _to_list(head) == [3, 2, 1]
    assert _to_list(insert_node_at_head(None, 7)) == [7]
