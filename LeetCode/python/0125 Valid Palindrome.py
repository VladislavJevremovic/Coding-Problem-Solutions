# https://leetcode.com/problems/valid-palindrome/


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        """Two pointers from both ends, skipping non-alphanumerics in place and
        comparing case-folded characters."""
        # Time: O(n)   Space: O(1)
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left].isalnum():
                right -= 1
            else:
                left += 1

        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        """Lower-case into a char list first, then two-pointer compare while
        skipping non-alphanumerics."""
        # Time: O(n)   Space: O(n)
        if not len(s):
            return True

        s_array = list(s.lower())
        n = len(s_array)

        a, b = 0, n - 1
        while a < b:
            # proceed from left ignoring non-alphanumeric characters
            while a < n and not s_array[a].isalnum():
                a += 1

            # proceed from right ignoring non-alphanumeric characters
            while b >= 0 and not s_array[b].isalnum():
                b -= 1

            if a >= n or b < 0:
                return True

            if s_array[a] != s_array[b]:
                return False

            a += 1
            b -= 1

        return True


def test():
    s = Solution2()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
