# https://leetcode.com/problems/rotate-list

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head

        counter = head
        length = 0
        while counter:
            length += 1
            tail = counter
            counter = counter.next

        if length == 1:
            return head

        l_rotations = length - k % length

        result = head
        while l_rotations > 0:
            chopped_head = result
            remainder = result.next

            chopped_head.next = None
            tail.next = chopped_head
            tail = tail.next

            result = remainder
            l_rotations -= 1

        return result

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
