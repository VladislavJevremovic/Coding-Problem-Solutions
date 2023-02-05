# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True
        else:
            return self.isPowerOfFour(num // 4) if not num % 4 else False

        # return num > 0 and not num & (num - 1) and not (num & 0b10101010101010101010101010101010)


def test():
    s = Solution()
    assert s.isPowerOfFour(16) is True
    assert s.isPowerOfFour(5) is False
