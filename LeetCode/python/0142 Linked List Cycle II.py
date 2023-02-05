# https://leetcode.com/problems/linked-list-cycle-ii/

from python.Helpers.SinglyLinkedList import *

ListNode = SinglyLinkedNode


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        visited = set()

        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None

# def test():
# s = Solution()

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
#
# Input: head = [1], pos = -1
# Output: no cycle
