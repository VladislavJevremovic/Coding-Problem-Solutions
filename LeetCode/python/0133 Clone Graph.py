# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Node) -> Node:
        """DFS the graph, memoizing each original node to its clone so shared
        and cyclic neighbors are copied exactly once."""
        # Time: O(V + E)   Space: O(V)
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        self.visited[node] = Node(node.val, [])

        if node.neighbors:
            for n in node.neighbors:
                self.visited[node].neighbors.append(self.cloneGraph(n))

        return self.visited[node]


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]

# Input: adjList = [[]]
# Output: [[]]
#
# Input: adjList = []
# Output: []
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]


def test():
    def neighbor_map(node):
        result = {}
        seen = set()
        stack = [node]
        while stack:
            n = stack.pop()
            if n.val in seen:
                continue
            seen.add(n.val)
            result[n.val] = sorted(x.val for x in n.neighbors)
            for x in n.neighbors:
                if x.val not in seen:
                    stack.append(x)
        return result

    def build():
        # Square graph: 1-2, 1-4, 2-3, 3-4
        n1 = Node(1, [])
        n2 = Node(2, [])
        n3 = Node(3, [])
        n4 = Node(4, [])
        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]
        return n1

    original = build()
    clone = Solution().cloneGraph(original)
    assert clone is not original
    assert neighbor_map(clone) == neighbor_map(original)
    assert neighbor_map(original) == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}

    assert Solution().cloneGraph(None) is None
