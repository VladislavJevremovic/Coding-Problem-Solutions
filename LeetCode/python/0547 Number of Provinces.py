# https://leetcode.com/problems/number-of-provinces/

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Count connected components in the adjacency matrix by running a DFS
        from each unvisited node."""
        # Time: O(n^2)   Space: O(n)
        n = len(isConnected)

        def dfs(M: List[List[int]], visited: List[int], i: int):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)

        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(isConnected, visited, i)
                count += 1

        return count


def test():
    s = Solution()
    assert s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
