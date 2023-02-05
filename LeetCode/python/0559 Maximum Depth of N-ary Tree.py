# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution1:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0

        depth, nodes = 0, [root]
        while nodes:
            depth += 1
            nodes = [child for node in nodes for child in node.children]

        return depth


class Solution2:
    def maxDepth(self, root: Node) -> int:
        def dfs(root):
            if not root.children:
                return 1
            else:
                return max(dfs(i) for i in root.children) + 1

        if not root:
            return 0

        return dfs(root)

# Input: root = [1,None,3,2,4,None,5,6]
# Output: 3
# Example 2:
#
#
#
# Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# Output: 5
