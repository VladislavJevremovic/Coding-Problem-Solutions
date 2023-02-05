# https://leetcode.com/problems/integer-break/

# Maximize f=x(N-x), x=N/2 (derivative=0); (N/2)*(N/2) when N even, (N-1)/2 *(N+1)/2 when N odd
# Break when max(f) >= N: (N/2)*(N/2)>=N, N>=4; (N-1)/2 *(N+1)/2>=N, N>=5
# Thus use 2 and 3 (prefer 3)

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        if n == 3:
            return 2

        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n  # remainder

        return product


def test():
    s = Solution()
    assert s.integerBreak(2) == 1
    assert s.integerBreak(10) == 36
