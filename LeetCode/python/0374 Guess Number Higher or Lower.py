# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def __init__(self, pick):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num < self.pick:
            return 1
        elif num > self.pick:
            return -1

        return 0

    def guessNumber(self, n: int) -> int:
        a = 1
        b = n
        while a <= b:
            m = a + (b - a) // 2
            r = self.guess(m)
            if r > 0:
                a = m + 1
            elif r < 0:
                b = m - 1
            else:
                return m

        return -1


def test():
    s = Solution(6)
    assert s.guessNumber(10) == 6

    s = Solution(1)
    assert s.guessNumber(1) == 1

    s = Solution(2)
    assert s.guessNumber(2) == 2
