# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * n  # [i]: cost from i to i + 1 or i + 2
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]
        for i in range(2, len(cost)):
            t = cost[i] + min(a, b)
            a, b = b, t

        return min(a, b)


def test():
    s = Solution2()
    assert s.minCostClimbingStairs([10, 15]) == 10
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
