# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # l, r : define reversing range
    # pre, cur : used in reversing, standard reverse linked linked list method
    # jump : used to connect last node in previous k-group to first node in following k-group

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
