# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sentinel = ListNode(0, head)
        p = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                p.next = head.next  # next after latest head repetition
            else:
                p = p.next  # move to next/different one, head does not repeat (anymore)

            head = head.next

        return sentinel.next


def test():
    def case(list1: List[int], output: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().deleteDuplicates(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(output)

    assert case([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
    assert case([1, 1, 1, 2, 3], [2, 3])
