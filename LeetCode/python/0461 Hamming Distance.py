# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Walk the bits of both numbers in lockstep, counting positions where
        they differ."""
        # Time: O(b)   Space: O(1)   (b = number of bits)
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
