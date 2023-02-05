# https://leetcode.com/problems/add-two-numbers

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        head = dummy_head
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            head.next = ListNode(carry % 10)
            head = head.next

            carry //= 10

        if carry:
            head.next = ListNode(carry)

        return dummy_head.next


def test():
    def case(list1: List[int], list2: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().addTwoNumbers(SinglyLinkedList.from_sequence(list1).head,
                                     SinglyLinkedList.from_sequence(list2).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([2, 4, 3], [5, 6, 4], [7, 0, 8])
    assert case([0], [0], [0])
    assert case([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
