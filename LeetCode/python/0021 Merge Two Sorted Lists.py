# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Recursively pick the smaller head and splice the merge of the rest
        behind it."""
        # Time: O(m + n)   Space: O(m + n) recursion depth
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1, l2.next)

        return temp


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]


def test():
    def case(list1: List[int], list2: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().mergeTwoLists(
                SinglyLinkedList.from_sequence(list1).head,
                SinglyLinkedList.from_sequence(list2).head,
            )
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    assert case([], [], [])
    assert case([], [0], [0])
    assert case([5], [], [5])
