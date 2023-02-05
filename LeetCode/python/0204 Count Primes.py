# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:
                i = p * p
                while i < n:
                    is_prime[i] = False
                    i += p
            p += 1

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1

        return count


def test():
    s = Solution()
    assert s.countPrimes(0) == 0
    assert s.countPrimes(1) == 0
    assert s.countPrimes(2) == 0
    assert s.countPrimes(3) == 1
    assert s.countPrimes(10) == 4
    assert s.countPrimes(20) == 8
