# https://leetcode.com/problems/delete-node-in-a-linked-list/

from typing import List

from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode


class Solution:
    def deleteNode(self, node):
        """Given only the node to delete, copy each successor's value forward and
        unlink the final node, effectively shifting the list left over it."""
        # Time: O(n)   Space: O(1)
        processed_node = None
        while node and node.next:
            node.val = node.next.val
            processed_node = node
            node = node.next
        processed_node.next = None


# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
#
# Input: head = [1,2,3,4], node = 3
# Output: [1,2,4]
#
# Input: head = [0,1], node = 0
# Output: [1]
#
# Input: head = [-3,5,-99], node = -3
# Output: [5,-99]


def test():
    def case(list1: List[int], val: int, expected: List[int]) -> bool:
        head = None
        target = None
        for v in reversed(list1):
            head = SinglyLinkedNode(v, head)
            if v == val:
                target = head

        Solution().deleteNode(target)

        return SinglyLinkedList(head) == SinglyLinkedList.from_sequence(expected)

    assert case([4, 5, 1, 9], 5, [4, 1, 9])
    assert case([4, 5, 1, 9], 1, [4, 5, 9])
    assert case([1, 2, 3, 4], 3, [1, 2, 4])
    assert case([0, 1], 0, [1])
    assert case([-3, 5, -99], -3, [5, -99])
