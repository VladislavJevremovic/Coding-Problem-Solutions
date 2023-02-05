# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List


# Zero in-degree nodes: all must be in result (can't be reached, others can); O(E), O(N)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(j for i, j in edges))


def test():
    s = Solution()
    assert s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]
    assert s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]
