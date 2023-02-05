# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []

        r = [root.val]
        for child in root.children:
            r += self.preorder(child)

        return r

# Input: root = [1,None,3,2,4,None,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:
#
#
#
# Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
