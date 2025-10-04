# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, n: int) -> str:
        """Repeatedly take n mod 26 as the next letter (bijective base-26),
        carrying down for the 'Z' case where the remainder is 0."""
        # Time: O(log n)   Space: O(log n)
        result = []
        while n:
            r = n % 26
            n //= 26
            if not r:
                if n >= 1:
                    r = 26
                n -= 1  # n = r + 26 * (1 + 26 * (1 + ...

            c = chr(ord("A") + r - 1)
            result.insert(0, c)

        return "".join(result)


def test():
    s = Solution()
    assert s.convertToTitle(1) == "A"
    assert s.convertToTitle(2) == "B"
    assert s.convertToTitle(3) == "C"
    assert s.convertToTitle(26) == "Z"
    assert s.convertToTitle(27) == "AA"
    assert s.convertToTitle(28) == "AB"
    assert s.convertToTitle(701) == "ZY"
    assert s.convertToTitle(702) == "ZZ"
