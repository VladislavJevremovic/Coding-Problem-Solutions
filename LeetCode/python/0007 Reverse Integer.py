# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x

        result = 0
        sign = x // abs(x)
        x = abs(x)
        while x > 0:
            result = 10 * result + x % 10
            x //= 10

        signed_result = sign * result
        not_32_bit = signed_result < -2 ** 31 or signed_result > 2 ** 31 - 1
        return 0 if not_32_bit else signed_result


def test():
    s = Solution()
    assert s.reverse(0) == 0
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0
    assert s.reverse(1563847412) == 0
