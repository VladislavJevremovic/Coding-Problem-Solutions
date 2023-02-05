# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
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
