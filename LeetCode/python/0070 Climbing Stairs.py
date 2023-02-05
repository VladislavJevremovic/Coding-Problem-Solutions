# https://leetcode.com/problems/climbing-stairs/

class Solution1:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]


class Solution2:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n - 1):
            t = a + b
            a = b
            b = t

        return b


def test():
    s = Solution1()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
