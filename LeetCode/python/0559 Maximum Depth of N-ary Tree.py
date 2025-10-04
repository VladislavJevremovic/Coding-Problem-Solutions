# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution1:
    def maxDepth(self, root: Node) -> int:
        """Iterative BFS counting how many full levels the tree contains."""
        # Time: O(n)   Space: O(n)
        if not root:
            return 0

        depth, nodes = 0, [root]
        while nodes:
            depth += 1
            nodes = [child for node in nodes for child in node.children]

        return depth


class Solution2:
    def maxDepth(self, root: Node) -> int:
        """Recursive DFS: depth is 1 plus the max depth among the children."""

        # Time: O(n)   Space: O(h)   (recursion stack; h = tree height)
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


def test():
    def build():
        n5, n6 = Node(5, []), Node(6, [])
        n3 = Node(3, [n5, n6])
        n2 = Node(2, [])
        n4 = Node(4, [])
        return Node(1, [n3, n2, n4])

    assert Solution1().maxDepth(build()) == 3
    assert Solution2().maxDepth(build()) == 3
    assert Solution1().maxDepth(None) == 0
    assert Solution2().maxDepth(None) == 0
