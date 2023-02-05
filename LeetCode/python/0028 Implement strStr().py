# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0

        if haystack and not needle:
            return 0

        if needle and not haystack:
            return -1

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


def test():
    s = Solution()
    assert s.strStr("", "") == 0
    assert s.strStr("hello", "") == 0
    assert s.strStr("", "hello") == -1
    assert s.strStr("hello", "ll") == 2
    assert s.strStr("aaaaa", "bba") == -1
