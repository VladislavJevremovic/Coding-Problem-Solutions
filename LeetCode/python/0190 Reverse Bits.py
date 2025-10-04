# https://leetcode.com/problems/reverse-bits/


class Solution1:
    def reverseBits(self, n: int) -> int:
        """Pull bits off the low end of n and shift them into r from the low end,
        reversing the 32-bit order via arithmetic."""
        # Time: O(1)   Space: O(1)  (fixed 32 iterations)
        r = 0
        for _ in range(32):
            r = r * 2 + int(n % 2)
            n /= 2

        return r


class Solution2:
    def reverseBits(self, n: int) -> int:
        """Shift r left and OR in n's lowest bit each step, building the reverse
        with bit operations."""
        # Time: O(1)   Space: O(1)  (fixed 32 iterations)
        r = 0
        for _ in range(32):
            r <<= 1
            r |= n & 1
            n >>= 1

        return r


def test():
    s = Solution2()
    assert (
        s.reverseBits(0b00000010100101000001111010011100)
        == 0b00111001011110000010100101000000
    )
    assert (
        s.reverseBits(0b11111111111111111111111111111101)
        == 0b10111111111111111111111111111111
    )
