# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# HackerRank: Reverse a linked list
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """Iteratively flip each node's next pointer to its predecessor in one pass."""
    # Time: O(n)   Space: O(1)
    prev: Optional[ListNode] = None
    while head is not None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


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
    assert _to_list(reverse(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert _to_list(reverse(_build([1]))) == [1]
    assert reverse(None) is None
    assert _to_list(reverse(_build([7, 8]))) == [8, 7]
