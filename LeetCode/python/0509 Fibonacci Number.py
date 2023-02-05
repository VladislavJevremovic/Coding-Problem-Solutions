# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        for _ in range(N):
            t = a + b
            a = b
            b = t

        return a


def test():
    s = Solution()
    assert s.fib(2) == 1
    assert s.fib(3) == 2
    assert s.fib(4) == 3
