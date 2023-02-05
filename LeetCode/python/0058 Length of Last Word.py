# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = 0
        spaced = False
        for c in s:
            if c != ' ':
                if spaced:
                    r = 1
                else:
                    r += 1
                spaced = False
            else:
                spaced = True

        return r


def test():
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord(" ") == 0
    assert s.lengthOfLastWord("a ") == 1
    assert s.lengthOfLastWord("a") == 1
    assert s.lengthOfLastWord(" a") == 1
    assert s.lengthOfLastWord("Today is a nice day") == 3
