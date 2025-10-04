# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """DP over substrings: s[i:j] is a palindrome iff its ends match and the
        inner substring is one, tracking the longest seen."""
        # Time: O(n^2)   Space: O(n^2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # result at [i:j] substring

        result = ""
        for i in range(n - 1, -1, -1):  # check upper triangle half (j >= i)
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True  # single character
                elif s[i] == s[j]:
                    dp[i][j] = (i + 1 == j) or dp[i + 1][
                        j - 1
                    ]  # true if 2-char or based on previous

                if dp[i][j] and (j - i + 1) > len(result):  # longer candidate?
                    result = s[i : j + 1]  # store new maximum

        return result


def test():
    s = Solution()
    assert s.longestPalindrome("babad") in ["aba", "bab"]
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ac") in ["a", "c"]
