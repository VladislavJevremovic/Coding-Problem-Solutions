# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                q.extend(node.children)

            result.append(level)

        return result

# Input: root = [1,None,3,2,4,None,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
