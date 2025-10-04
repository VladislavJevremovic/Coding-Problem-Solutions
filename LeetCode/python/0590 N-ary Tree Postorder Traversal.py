# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        """Recursive postorder: recurse over all children first, then append the
        node's value."""
        # Time: O(n)   Space: O(h)   (recursion stack; h = tree height)
        if not root:
            return []

        r = []
        for child in root.children:
            r += self.postorder(child)

        return r + [root.val]


# Input: root = [1,None,3,2,4,None,5,6]
# Output: [5,6,3,2,4,1]
# Example 2:
#
#
# Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


def test():
    def build():
        n5, n6 = Node(5, []), Node(6, [])
        n3 = Node(3, [n5, n6])
        n2 = Node(2, [])
        n4 = Node(4, [])
        return Node(1, [n3, n2, n4])

    assert Solution().postorder(build()) == [5, 6, 3, 2, 4, 1]
    assert Solution().postorder(None) == []
