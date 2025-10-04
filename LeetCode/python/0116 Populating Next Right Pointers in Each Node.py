# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        """BFS level by level, wiring each node's next pointer to the node that
        follows it in the same level's queue."""
        # Time: O(n)   Space: O(n)
        if not root:
            return root

        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i < n - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root


# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
#
# Input: root = []
# Output: []


def test():
    def build():
        n4, n5, n6, n7 = Node(4), Node(5), Node(6), Node(7)
        n2 = Node(2, n4, n5)
        n3 = Node(3, n6, n7)
        return Node(1, n2, n3)

    root = Solution().connect(build())
    assert root.next is None
    assert root.left.next is root.right
    assert root.right.next is None
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is root.right.right
    assert root.right.right.next is None

    assert Solution().connect(None) is None
