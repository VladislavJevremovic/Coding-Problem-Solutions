# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

from python.Helpers.SinglyLinkedList import SinglyLinkedNode

ListNode = SinglyLinkedNode


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        """Walk the list recording visited nodes; the first node seen twice is
        where the cycle begins."""
        # Time: O(n)   Space: O(n)
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
