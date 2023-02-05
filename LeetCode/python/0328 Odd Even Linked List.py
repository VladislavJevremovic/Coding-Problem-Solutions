# https://leetcode.com/problems/odd-even-linked-list/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_list = ListNode(0)
        even_list = ListNode(0)

        odd_head = odd_list
        even_head = even_list

        is_odd = True
        while head:
            if is_odd:
                odd_list.next = head
                odd_list = odd_list.next
            else:
                even_list.next = head
                even_list = even_list.next

            is_odd = not is_odd
            head = head.next

        even_list.next = None
        odd_list.next = even_head.next

        return odd_head.next


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().oddEvenList(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], [1, 3, 5, 2, 4])
    assert case([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
