# https://leetcode.com/problems/find-the-town-judge/

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n

        inout_trust = [[0, 0] for _ in range(n)]  # [in, out]
        for t in trust:
            inout_trust[t[1] - 1][0] += 1
            inout_trust[t[0] - 1][1] += 1

        for i, t in enumerate(inout_trust):
            if t[0] == n - 1 and t[1] == 0:
                return i + 1

        return -1


def test():
    s = Solution()
    assert s.findJudge(1, []) == 1
    assert s.findJudge(2, [[1, 2]]) == 2
    assert s.findJudge(3, [[1, 3], [2, 3]]) == 3
    assert s.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
    assert s.findJudge(3, [[1, 2], [2, 3]]) == -1
    assert s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
