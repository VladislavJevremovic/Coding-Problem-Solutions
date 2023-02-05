# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        return n // 5 + self.trailingZeroes(n // 5)


def test():
    s = Solution()
    assert s.trailingZeroes(3) == 0
    assert s.trailingZeroes(5) == 1
