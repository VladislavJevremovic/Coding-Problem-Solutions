# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        while n:
            w += n & 1
            n >>= 1

        return w


def test():
    s = Solution()
    assert s.hammingWeight(0b00000000000000000000000000001011) == 3
    assert s.hammingWeight(0b00000000000000000000000010000000) == 1
    assert s.hammingWeight(0b11111111111111111111111111111101) == 31
