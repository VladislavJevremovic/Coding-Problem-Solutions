# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        """Digital root via the closed-form: the result is num mod 9, treating an
        exact multiple of 9 (and only nonzero num) as 9."""
        # Time: O(1)   Space: O(1)
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9


def test():
    s = Solution()
    assert s.addDigits(38) == 2
    assert s.addDigits(0) == 0
