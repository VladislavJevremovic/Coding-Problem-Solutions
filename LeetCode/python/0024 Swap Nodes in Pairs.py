# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import List, Optional

from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode

ListNode = SinglyLinkedNode


class Solution1:  # recursive
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive: swap the first pair, then let recursion swap the rest and
        link it behind them."""
        # Time: O(n)   Space: O(n) recursion depth
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


class Solution2:  # iterative
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative: walk the list behind a dummy, relinking each adjacent pair
        in place via a trailing prev pointer."""
        # Time: O(n)   Space: O(1)
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return dummy.next


def test():
    def case(list1: List[int], expected: List[int]) -> bool:
        return SinglyLinkedList(
            Solution1().swapPairs(SinglyLinkedList.from_sequence(list1).head)
        ) == SinglyLinkedList.from_sequence(expected)

    assert case([1, 2, 3, 4], [2, 1, 4, 3])
    assert case([], [])
    assert case([1], [1])
