# https://leetcode.com/problems/middle-of-the-linked-list

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode

ListNode = SinglyLinkedNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """Two-pointer scan: the slow pointer lands on the middle when the fast
        pointer (double speed) runs off the end."""
        # Time: O(n)   Space: O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().middleNode(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], [3, 4, 5])
    assert case([1, 2, 3, 4, 5, 6], [4, 5, 6])
