# https://leetcode.com/problems/all-paths-from-source-to-target/

from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []

        def backtrack(current_node: int, path):
            if current_node == target:
                result.append(list(path))
                return

            for next_node in graph[current_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = deque([0])
        backtrack(0, path)

        return result


def test():
    s = Solution()
    assert s.allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    assert s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == \
           [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert s.allPathsSourceTarget([[1], []]) == [[0, 1]]
    assert s.allPathsSourceTarget([[1, 2, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
    assert s.allPathsSourceTarget([[1, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 3]]
