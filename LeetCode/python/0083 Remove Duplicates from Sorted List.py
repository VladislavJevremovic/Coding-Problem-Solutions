# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import List, Optional

from python.Helpers.SinglyLinkedList import SinglyLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Single pass: unlink each node whose value equals its successor's,
        keeping one copy of every value."""
        # Time: O(n)   Space: O(1)
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# Input: head = [1,1,2]
# Output: [1,2]
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().deleteDuplicates(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 1, 2], [1, 2])
    assert case([1, 1, 2, 3, 3], [1, 2, 3])
    assert case([], [])
    assert case([1], [1])
    assert case([2, 2, 2], [2])
