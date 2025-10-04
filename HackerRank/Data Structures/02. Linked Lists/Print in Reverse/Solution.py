# https://www.hackerrank.com/challenges/print-in-reverse/problem
# HackerRank: Print in Reverse
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def reverse_print(head: Optional[ListNode]) -> List[int]:
    """Recurse to the tail, then append each value on the way back to reverse order."""
    # Time: O(n)   Space: O(n)  (recursion depth + output list)
    if head is None:
        return []
    return reverse_print(head.next) + [head.val]


def _build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def test() -> None:
    assert reverse_print(_build([1, 2, 3, 4])) == [4, 3, 2, 1]
    assert reverse_print(_build([5])) == [5]
    assert reverse_print(None) == []
