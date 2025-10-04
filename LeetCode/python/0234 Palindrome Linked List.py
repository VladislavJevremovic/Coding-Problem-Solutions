# https://leetcode.com/problems/palindrome-linked-list/

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode

ListNode = SinglyLinkedNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """Push all values onto a stack, then walk the list again comparing each
        node against the stack's pop (the list read in reverse)."""
        # Time: O(n)   Space: O(n)
        if not head:
            return True

        stack = []

        p = head
        while p:
            stack.append(p.val)
            p = p.next

        p = head
        while p:
            t = stack.pop()
            if t != p.val:
                return False
            p = p.next

        return True


def test():
    def case(list1: List[int], expected: bool) -> bool:
        return (
            Solution().isPalindrome(SinglyLinkedList.from_sequence(list1).head)
            is expected
        )

    assert case([1, 2, 2, 1], True)
    assert case([1, 2], False)
