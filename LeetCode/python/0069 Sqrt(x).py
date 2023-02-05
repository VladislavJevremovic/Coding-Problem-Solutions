# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        a = 2
        b = x // 2
        while a < b:
            m = a + (b - a) // 2
            if m * m > x:
                b = m - 1
            elif m * m < x:
                if (m + 1) * (m + 1) > x:
                    return m
                a = m + 1
            else:
                return m

        return b


def test():
    s = Solution()
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    assert s.mySqrt(2) == 1
    assert s.mySqrt(3) == 1
    assert s.mySqrt(4) == 2
    assert s.mySqrt(5) == 2
    assert s.mySqrt(6) == 2
    assert s.mySqrt(7) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(9) == 3
