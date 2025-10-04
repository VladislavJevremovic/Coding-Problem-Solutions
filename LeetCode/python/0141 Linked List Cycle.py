# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """Floyd's tortoise and hare: a fast pointer laps a slow one iff a cycle
        exists."""
        # Time: O(n)   Space: O(1)
        if not head:
            return False

        slow_p = fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True

        return False


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false


def test():
    def build(vals):
        head = None
        prev = None
        nodes = []
        for v in vals:
            node = ListNode(v)
            nodes.append(node)
            if prev:
                prev.next = node
            else:
                head = node
            prev = node
        return head, nodes

    # Cyclic: tail connects back to node at index 1.
    head, nodes = build([3, 2, 0, -4])
    nodes[-1].next = nodes[1]
    assert Solution().hasCycle(head) is True

    # Acyclic chain.
    head, _ = build([3, 2, 0, -4])
    assert Solution().hasCycle(head) is False

    # Empty list.
    assert Solution().hasCycle(None) is False

    # Single node, no cycle.
    head, _ = build([1])
    assert Solution().hasCycle(head) is False
