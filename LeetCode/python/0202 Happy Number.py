# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        """Repeatedly replace n by the sum of squares of its digits, tracking
        seen values in a set to detect a cycle (unhappy) versus reaching 1."""

        # Time: O(log n) per step, bounded total   Space: O(log n)
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2

            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


def test():
    s = Solution()
    assert s.isHappy(19) is True
    assert s.isHappy(2) is False
