# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """DP grid where each cell's path count is the sum of the cell above and
        the cell to its left, with the top row and left column seeded to 1."""
        # Time: O(m * n)   Space: O(m * n)
        dp = [[1] * n for _ in range(m)]  # we'll fix for m, n > 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


def test():
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(7, 3) == 28
    assert s.uniquePaths(3, 3) == 6
