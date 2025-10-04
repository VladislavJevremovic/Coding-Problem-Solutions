# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """One pass with two pointers spaced n+1 apart, so when the fast pointer
        runs off the end the slow pointer sits just before the target."""
        # Time: O(L)   Space: O(1)
        dummy = ListNode(0)
        dummy.next = head

        fast_p = slow_p = dummy
        for _ in range(1, n + 2):
            fast_p = fast_p.next

        while fast_p:
            fast_p = fast_p.next
            slow_p = slow_p.next

        slow_p.next = slow_p.next.next

        return dummy.next


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]


def test():
    def case(list1: List[int], n: int, expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().removeNthFromEnd(SinglyLinkedList.from_sequence(list1).head, n)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    assert case([1], 1, [])
    assert case([1, 2], 1, [1])
    assert case([1, 2], 2, [2])
