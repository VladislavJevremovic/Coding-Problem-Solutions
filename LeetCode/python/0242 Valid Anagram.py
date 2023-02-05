# https://leetcode.com/problems/valid-anagram/

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return len(s) == len(t) and sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = [0] * 26

        for c in s:
            d[ord(c) - ord("a")] += 1

        for c in t:
            d[ord(c) - ord("a")] -= 1

        for c in d:
            if c:
                return False

        return True


def test():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
