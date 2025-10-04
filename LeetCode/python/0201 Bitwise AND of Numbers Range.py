# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """Right-shift both bounds until they meet on their common binary
        prefix; the differing low bits AND to zero, so shift the prefix back."""
        # Time: O(log right)   Space: O(1)
        shift = 0
        while left < right:  # find common bitwise prefix (rest is zeros)
            left = left >> 1
            right = right >> 1
            shift += 1

        return left << shift  # shift back to get actual result


def test():
    s = Solution()
    assert s.rangeBitwiseAnd(5, 7) == 4
    assert s.rangeBitwiseAnd(0, 1) == 0
    assert s.rangeBitwiseAnd(1, 2147483647) == 0
