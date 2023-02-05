# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:
        multiplier = 1
        result = 0
        for c in reversed(list(s)):
            difference = ord(c) - ord("A")
            result += (difference + 1) * multiplier  # A = 1
            multiplier *= 26

        return result


def test():
    s = Solution()
    assert s.titleToNumber("A") == 1
    assert s.titleToNumber("B") == 2
    assert s.titleToNumber("C") == 3
    assert s.titleToNumber("Z") == 26
    assert s.titleToNumber("AA") == 27
    assert s.titleToNumber("AB") == 28
    assert s.titleToNumber("ZY") == 701
    assert s.titleToNumber("ZZ") == 702
