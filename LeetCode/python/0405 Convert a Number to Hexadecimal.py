# https://leetcode.com/problems/shuffle-string/


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = num + (2 ** 32)

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
