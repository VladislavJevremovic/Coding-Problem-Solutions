# https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        """DP from the right: ways to decode from i is ways from i+1 plus, when
        s[i:i+2] is a valid 10-26 code, ways from i+2."""
        # Time: O(n)   Space: O(n)
        n = len(s)

        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != "0":  # skip leading zeros
                dp[i] = dp[i + 1]
                if i < n - 1 and (
                    s[i] == "1" or s[i] == "2" and s[i + 1] < "7"
                ):  # up to 26
                    dp[i] += dp[i + 2]

        return dp[0]


def test():
    s = Solution()
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("0") == 0
    assert s.numDecodings("06") == 0
