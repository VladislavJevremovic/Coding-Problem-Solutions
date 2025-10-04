# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution1:
    def tribonacci(self, n: int) -> int:
        """Bottom-up DP filling a table where each term is the sum of the prior three."""
        # Time: O(n)   Space: O(n)
        if n == 0:
            return 0

        if n <= 2:
            return 1

        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        f[2] = 1

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2] + f[i - 3]

        return f[n]


class Solution2:
    def tribonacci(self, n: int) -> int:
        """Same recurrence with three rolling variables instead of a table."""
        # Time: O(n)   Space: O(1)
        a = 0
        b = 1
        c = 1
        for _ in range(n):
            t = a + b + c
            a = b
            b = c
            c = t

        return a


def test():
    s = Solution1()
    assert s.tribonacci(0) == 0
    assert s.tribonacci(1) == 1
    assert s.tribonacci(2) == 1
    assert s.tribonacci(3) == 2
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537
