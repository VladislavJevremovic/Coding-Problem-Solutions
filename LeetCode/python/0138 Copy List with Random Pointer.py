# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Node) -> Optional[Node]:
        """Recursively clone nodes, memoizing original->copy so each node and
        its next/random pointers are duplicated exactly once."""
        # Time: O(n)   Space: O(n)
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        new_node = Node(head.val)
        self.visited[head] = new_node

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node


# Input: head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,None],[13,0],[11,4],[10,2],[1,0]]
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
# Input: head = [[3,None],[3,0],[3,None]]
# Output: [[3,None],[3,0],[3,None]]
#
# Input: head = []
# Output: []


def test():
    def build():
        # vals [7, 13, 11, 10, 1], random by index: [None, 0, 4, 2, 0]
        nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        randoms = [None, 0, 4, 2, 0]
        for i, r in enumerate(randoms):
            nodes[i].random = nodes[r] if r is not None else None
        return nodes[0]

    head = build()
    copy = Solution().copyRandomList(head)

    # Collect originals in order for index lookups.
    orig_nodes = []
    n = head
    while n:
        orig_nodes.append(n)
        n = n.next

    a, b = head, copy
    while a:
        assert b is not None
        assert b is not a
        assert b.val == a.val
        if a.random is None:
            assert b.random is None
        else:
            idx = orig_nodes.index(a.random)
            assert b.random is not a.random
            assert b.random.val == a.random.val
            # The copy's random must point to the copy at the same index.
            cnode = copy
            for _ in range(idx):
                cnode = cnode.next
            assert b.random is cnode
        a, b = a.next, b.next
    assert b is None

    assert Solution().copyRandomList(None) is None
