# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """DP over prefixes: dp[i] is True when some split point j has dp[j] set
        and s[j:i] is a dictionary word."""
        # Time: O(n^3)   Space: O(n)  (n^2 substrings, each O(n) to slice/hash)
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # index j splits s[:i] into s[:j] and s[j:i]
        dp[0] = True  # empty always in set

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


def test():
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) is True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
