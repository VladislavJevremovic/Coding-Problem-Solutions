# https://www.hackerrank.com/challenges/delete-a-node/problem
# HackerRank: Delete a Node
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def delete_node(head: Optional[ListNode], position: int) -> Optional[ListNode]:
    """Advance to the predecessor of the target index and splice out that node."""
    # Time: O(position)   Space: O(1)
    if head is None:
        return None
    if position == 0:
        return head.next
    prev = head
    for _ in range(position - 1):
        assert prev.next is not None
        prev = prev.next
    if prev.next is not None:
        prev.next = prev.next.next
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
    assert _to_list(delete_node(_build([1, 2, 3, 4]), 0)) == [2, 3, 4]
    assert _to_list(delete_node(_build([1, 2, 3, 4]), 2)) == [1, 2, 4]
    assert _to_list(delete_node(_build([1, 2, 3, 4]), 3)) == [1, 2, 3]
    assert _to_list(delete_node(_build([5]), 0)) == []
    assert delete_node(None, 0) is None
