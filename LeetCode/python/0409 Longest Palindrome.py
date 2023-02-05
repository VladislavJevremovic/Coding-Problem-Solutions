# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in Counter(s).values())  # How many letters with odd count?
        return len(s) - odds + bool(odds)


def test():
    s = Solution()
    assert s.longestPalindrome("abccccdd") == 7
    assert s.longestPalindrome("a") == 1
    assert s.longestPalindrome("bb") == 2
