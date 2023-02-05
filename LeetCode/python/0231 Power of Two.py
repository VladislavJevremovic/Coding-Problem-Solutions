# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        else:
            return self.isPowerOfTwo(n // 2) if not n % 2 else False

        # return n > 0 and not (n & n - 1)


def test():
    s = Solution()
    assert s.isPowerOfTwo(1) is True
    assert s.isPowerOfTwo(16) is True
    assert s.isPowerOfTwo(3) is False
    assert s.isPowerOfTwo(4) is True
    assert s.isPowerOfTwo(5) is False
