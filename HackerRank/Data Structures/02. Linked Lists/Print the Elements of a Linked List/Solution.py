# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
# HackerRank: Print the Elements of a Linked List
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def print_linked_list(head: Optional[ListNode]) -> List[int]:
    """Traverse the list head to tail, collecting each node's value in order."""
    # Time: O(n)   Space: O(n)
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def _build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def test() -> None:
    assert print_linked_list(_build([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert print_linked_list(_build([42])) == [42]
    assert print_linked_list(None) == []
