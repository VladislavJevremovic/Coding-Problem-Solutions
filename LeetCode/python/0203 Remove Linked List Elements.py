# https://leetcode.com/problems/remove-linked-list-elements/


from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution1:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head


class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next


def test():
    def case(list1: List[int], val: int, expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution1().removeElements(SinglyLinkedList.from_sequence(list1).head, val)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
    assert case([], 1, [])
    assert case([7, 7, 7, 7], 7, [])
