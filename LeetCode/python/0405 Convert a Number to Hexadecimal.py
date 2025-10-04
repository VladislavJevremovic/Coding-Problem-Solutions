# https://leetcode.com/problems/convert-a-number-to-hexadecimal/


class Solution:
    def toHex(self, num: int) -> str:
        """Repeatedly take num mod 16 to emit hex digits low-to-high; map
        negatives to their 32-bit two's-complement value first."""
        # Time: O(1)   Space: O(1)   (fixed 32-bit width)
        if num == 0:
            return "0"

        if num < 0:
            num = num + (2**32)

        r = ""
        digits = "0123456789abcdef"

        while num > 0:
            r = digits[num % 16] + r
            num = num // 16

        return r


def test():
    s = Solution()
    assert s.toHex(26) == "1a"
    assert s.toHex(-1) == "ffffffff"
