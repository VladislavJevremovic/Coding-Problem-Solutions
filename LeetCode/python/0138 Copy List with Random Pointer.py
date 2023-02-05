# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Node) -> Optional[Node]:
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
