# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        n, sign = 0, 1

        s = s.strip()
        for i, c in enumerate(s):
            if c.isdigit():
                n = 10 * n + int(c)

                if sign * n > INT_MAX:
                    return INT_MAX

                if sign * n < INT_MIN:
                    return INT_MIN
            elif i == 0 and c == "+":
                pass
            elif i == 0 and c == "-":
                sign = -1
            else:
                break

        return sign * n


def test():
    s = Solution()
    assert s.myAtoi("42") == 42
    assert s.myAtoi("   -42") == -42
    assert s.myAtoi("4193 with words") == 4193
    assert s.myAtoi("words and 987") == 0
    assert s.myAtoi("-91283472332") == -2147483648
