# https://www.hackerrank.com/challenges/get-node-value/problem
# HackerRank: Get Node Value
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def get_node(head: Optional[ListNode], position_from_tail: int) -> int:
    """Count the length, then walk forward to the node at the given offset from the tail."""
    # Time: O(n)   Space: O(1)
    # position_from_tail == 0 is the last node.
    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next

    runner = head
    for _ in range(length - 1 - position_from_tail):
        assert runner is not None
        runner = runner.next
    assert runner is not None
    return runner.val


def _build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def test() -> None:
    head = _build([1, 3, 5, 6])
    assert get_node(head, 0) == 6  # last
    assert get_node(head, 1) == 5
    assert get_node(head, 3) == 1  # first
    assert get_node(_build([10]), 0) == 10
