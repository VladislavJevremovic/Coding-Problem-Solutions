# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Reverse the whole number arithmetically and compare with the
        original; negatives and trailing zeros can't be palindromes."""
        # Time: O(log x)   Space: O(1)
        if x < 0:
            return False

        if x > 9 and not x % 10:
            return False

        original = x
        flipped = 0
        while x:
            flipped = 10 * flipped + x % 10
            x //= 10

        return original == flipped


def test():
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
