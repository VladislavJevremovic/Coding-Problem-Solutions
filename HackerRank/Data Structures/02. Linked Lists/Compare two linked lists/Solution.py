# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
# HackerRank: Compare two linked lists
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def compare_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> bool:
    """Walk both lists in lockstep, equal iff values match and both end together."""
    # Time: O(min(m, n))   Space: O(1)
    while head1 is not None and head2 is not None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    # Equal only if both ran out at the same time.
    return head1 is None and head2 is None


def _build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def test() -> None:
    assert compare_lists(_build([1, 2, 3]), _build([1, 2, 3])) is True
    assert compare_lists(_build([1, 2, 3]), _build([1, 2, 4])) is False
    assert compare_lists(_build([1, 2]), _build([1, 2, 3])) is False
    assert compare_lists(_build([1, 2, 3]), _build([1, 2])) is False
    assert compare_lists(None, None) is True
    assert compare_lists(_build([1]), None) is False
