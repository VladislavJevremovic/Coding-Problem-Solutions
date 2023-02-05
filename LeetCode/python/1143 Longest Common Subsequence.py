# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)
        if not m or not n:
            return 0

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(0, m):
            for j in range(0, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]


def test():
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    assert s.longestCommonSubsequence("ab", "ab") == 2
    assert s.longestCommonSubsequence("b", "b") == 1
    assert s.longestCommonSubsequence("a", "b") == 0
