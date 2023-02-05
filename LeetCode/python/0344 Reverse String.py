# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


def test():
    s = Solution()

    input = ["h", "e", "l", "l", "o"]
    s.reverseString(input)
    assert input == ["o", "l", "l", "e", "h"]

    input = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(input)
    assert input == ["h", "a", "n", "n", "a", "H"]
