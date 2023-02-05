# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        a = 1
        while a < num:
            a *= 2
            a += 1

        return a - num


def test():
    s = Solution()
    assert s.findComplement(5) == 2
    assert s.findComplement(1) == 0
    assert s.findComplement(0) == 1
