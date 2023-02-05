# https://leetcode.com/problems/first-bad-version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a, b = 1, n
        while a < b:
            m = a + (b - a) // 2
            if isBadVersion(m):
                b = m
            else:
                a = m + 1

        return a


def isBadVersion(version: int) -> bool:
    return version == 4


def test():
    s = Solution()
    assert s.firstBadVersion(5) == 4
