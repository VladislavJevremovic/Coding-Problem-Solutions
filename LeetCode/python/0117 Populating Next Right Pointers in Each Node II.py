# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import collections


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
        """BFS level by level (works for any tree, not just perfect ones),
        wiring each node's next pointer to the next node in its level queue."""
        # Time: O(n)   Space: O(n)
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()

                if i < size - 1:
                    node.next = Q[0]

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root


# Input: root = [1,2,3,4,5,None,7]
# Output: [1,#,2,3,#,4,5,7,#]
#
# Input: root = []
# Output: []


def test():
    def build():
        n4, n5, n7 = Node(4), Node(5), Node(7)
        n2 = Node(2, n4, n5)
        n3 = Node(3, None, n7)
        return Node(1, n2, n3)

    root = Solution().connect(build())
    assert root.next is None
    assert root.left.next is root.right
    assert root.right.next is None
    # Leaf level: 4 -> 5 -> 7 -> None
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.right
    assert root.right.right.next is None

    assert Solution().connect(None) is None
