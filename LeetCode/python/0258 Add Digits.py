# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9


def test():
    s = Solution()
    assert s.addDigits(38) == 2
    assert s.addDigits(0) == 0
