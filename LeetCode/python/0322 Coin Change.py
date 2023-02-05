# https://leetcode.com/problems/coin-change/

import math
from collections import deque
from typing import List


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)  # +1 coin, value of which is in [coin, amount]

        return dp[amount] if dp[amount] != math.inf else -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = {amount}
        while q:
            remainder, num_coins = q.popleft()
            if remainder == 0:
                return num_coins

            for coin in coins:
                if remainder - coin >= 0 and remainder - coin not in seen:
                    q.append((remainder - coin, num_coins + 1))
                    seen.add(remainder - coin)

        return -1


def test():
    s = Solution1()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
