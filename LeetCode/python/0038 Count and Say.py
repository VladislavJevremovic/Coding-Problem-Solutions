# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            s = self.say(s)

        return s

    def say(self, s: str) -> str:
        r = ""

        sa = list(s)
        i = 0
        while i < len(sa):
            count = 1
            while i + 1 < len(sa) and sa[i] == sa[i + 1]:  # leave space ahead for actual digit, sum same occurrences
                i += 1
                count += 1
            r += str(count) + sa[i]
            i += 1

        return r


def test():
    s = Solution()
    assert s.countAndSay(1) == "1"
    assert s.countAndSay(2) == "11"
    assert s.countAndSay(3) == "21"
    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(5) == "111221"
    assert s.countAndSay(6) == "312211"
    assert s.countAndSay(7) == "13112221"
    assert s.countAndSay(8) == "1113213211"
