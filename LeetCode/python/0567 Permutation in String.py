# https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Slide a window of length len(s1) over s2, comparing 26-letter counts
        to detect a matching permutation."""
        # Time: O(n)   Space: O(1)   (fixed 26-letter arrays)
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False

        f1 = [0] * 26
        f2 = [0] * 26
        for i in range(l1):
            f1[ord(s1[i]) - ord("a")] += 1
            f2[ord(s2[i]) - ord("a")] += 1

        for i in range(l2 - l1):
            if f1 == f2:
                return True

            f2[ord(s2[i]) - ord("a")] -= 1
            f2[ord(s2[i + l1]) - ord("a")] += 1

        return f1 == f2


def test():
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") is True
    assert s.checkInclusion("ab", "eidboaoo") is False
    assert s.checkInclusion("ab", "ba") is True
