# https://leetcode.com/problems/valid-anagram/


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return len(s) == len(t) and sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        """Count each letter of s in a fixed 26-slot array, subtract t's letters,
        and confirm every count returned to zero."""
        # Time: O(n)   Space: O(1)
        if len(s) != len(t):
            return False

        d = [0] * 26

        for c in s:
            d[ord(c) - ord("a")] += 1

        for c in t:
            d[ord(c) - ord("a")] -= 1

        return all(not c for c in d)


def test():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
