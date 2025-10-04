# https://leetcode.com/problems/rotate-list

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode

ListNode = SinglyLinkedNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """Measure the length, then move the last k%length nodes one at a time
        from the front to the back by relinking through the tail."""
        # Time: O(n)   Space: O(1)
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


def test():
    def case(list1: List[int], k: int, expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution().rotateRight(SinglyLinkedList.from_sequence(list1).head, k)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
    assert case([0, 1, 2], 4, [2, 0, 1])
    assert case([], 1, [])
    assert case([1], 99, [1])
