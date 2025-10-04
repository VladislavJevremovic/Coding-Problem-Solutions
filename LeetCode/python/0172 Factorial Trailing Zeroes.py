# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Count factors of 5 in n! (the limiting prime for trailing zeros) by
        summing n//5 + n//25 + ... recursively."""
        # Time: O(log n)   Space: O(log n)
        if n == 0:
            return 0

        return n // 5 + self.trailingZeroes(n // 5)


def test():
    s = Solution()
    assert s.trailingZeroes(3) == 0
    assert s.trailingZeroes(5) == 1
