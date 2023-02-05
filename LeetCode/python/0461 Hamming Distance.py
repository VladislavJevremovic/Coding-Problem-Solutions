# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                d += 1
            x >>= 1
            y >>= 1

        return d


def test():
    s = Solution()
    assert s.hammingDistance(1, 4) == 2
    assert s.hammingDistance(3, 1) == 1
