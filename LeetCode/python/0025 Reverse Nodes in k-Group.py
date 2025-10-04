# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import List, Optional

from python.Helpers.SinglyLinkedList import SinglyLinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # l, r : define reversing range
    # pre, cur : used in reversing, standard reverse linked linked list method
    # jump : used to connect last node in previous k-group to first node in following k-group

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Walk the list k nodes at a time; when a full group is found, reverse
        it in place and splice it between the surrounding groups."""
        # Time: O(n)   Space: O(1)
        dummy = jump = ListNode(0)
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:  # use right to locate the range
                right = right.next
                count += 1
            if count == k:  # reverse inner linked list
                prev, curr = right, left
                for _ in range(k):
                    curr.next, curr, prev = prev, curr.next, curr  # reverse
                jump.next, jump, left = prev, left, right  # connect two k-groups
            else:
                return dummy.next


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:
#
# Input: head = [1], k = 1
# Output: [1]


def test():
    def case(list1: List[int], k: int, expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().reverseKGroup(SinglyLinkedList.from_sequence(list1).head, k)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
    assert case([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
    assert case([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5])
    assert case([1], 1, [1])
