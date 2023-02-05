# https://leetcode.com/problems/reverse-linked-list/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        return prev


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head  # re-wire
        head.next = None

        return p


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution2().reverseList(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    assert case([1, 2], [2, 1])
    assert case([], [])
