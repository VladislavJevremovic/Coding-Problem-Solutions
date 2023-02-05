# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # p, s = 1, 0
        # while n:
        #     r = n % 10
        #     p *= r
        #     s += r
        #     n //= 10

        p, s, ns = 1, 0, str(n)
        for d in ns:
            r = int(d)
            p *= r
            s += r

        return p - s


def test():
    s = Solution()
    assert s.subtractProductAndSum(234) == 15
    assert s.subtractProductAndSum(4421) == 21
