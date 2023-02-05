# https://leetcode.com/problems/intersection-of-two-linked-lists/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA

# def test():
#     def case(list1: List[int], list2: List[int], expected: Optional[int]) -> bool:
#         list_a = SinglyLinkedList.from_sequence(list1)
#         list_b = SinglyLinkedList.from_sequence(list2)
#         intersection_node = Solution().getIntersectionNode(list_a.head, list_b.head)
#         return SinglyLinkedList(
#
#         ) == SinglyLinkedList.from_sequence(expected)
#
#     assert case()

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
