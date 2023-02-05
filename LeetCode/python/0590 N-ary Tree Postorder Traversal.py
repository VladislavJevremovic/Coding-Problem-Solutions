# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
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
