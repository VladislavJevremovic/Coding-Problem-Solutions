# https://leetcode.com/problems/complement-of-base-10-integer/

# Same problem as 0476 Number Complement: flip every bit within the number's
# own bit-width.


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Build an all-ones mask the width of n, then subtract to flip every bit."""
        # Time: O(log n)   Space: O(1)
        mask = 1
        while mask < n:
            mask = mask * 2 + 1

        return mask - n


def test():
    s = Solution()
    assert s.bitwiseComplement(5) == 2
    assert s.bitwiseComplement(7) == 0
    assert s.bitwiseComplement(10) == 5
    assert s.bitwiseComplement(0) == 1
    assert s.bitwiseComplement(1) == 0
