# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        p = ""
        for i, c in enumerate(word):
            if i > 0 and p.islower() and c.isupper():
                return False
            if i > 1 and p.isupper() and c.islower():
                return False
            p = c

        return True


def test():
    s = Solution()
    assert s.detectCapitalUse("USA") is True
    assert s.detectCapitalUse("leetcode") is True
    assert s.detectCapitalUse("Google") is True
    assert s.detectCapitalUse("FlaG") is False
    assert s.detectCapitalUse("") is True
    assert s.detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf") is False
    assert s.detectCapitalUse("Leetcode") is True
