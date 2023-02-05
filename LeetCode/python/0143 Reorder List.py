# https://leetcode.com/problems/reorder-list/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        # find the middle of linked list [876]; in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [206]; convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists [21]; 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        linked_list = SinglyLinkedList.from_sequence(list1)
        Solution().reorderList(linked_list.head)

        return linked_list == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4], [1, 4, 2, 3])
    assert case([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
