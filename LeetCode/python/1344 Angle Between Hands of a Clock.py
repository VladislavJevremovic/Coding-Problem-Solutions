# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        r = abs(30 * (hour % 12) - 5.5 * minutes)
        return r if r <= 180 else 360 - r


def test():
    s = Solution()
    assert s.angleClock(12, 30) == 165
    assert s.angleClock(3, 30) == 75
    assert s.angleClock(3, 15) == 7.5
    assert s.angleClock(4, 50) == 155
    assert s.angleClock(12, 0) == 0
    assert s.angleClock(1, 57) == 76.5
