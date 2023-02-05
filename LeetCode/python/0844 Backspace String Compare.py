# https://leetcode.com/problems/backspace-string-compare/

class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def make_string(s):
            r = []
            for c in s:
                if c != '#':
                    r.append(c)
                elif r:
                    r.pop()

            return "".join(r)

        return make_string(S) == make_string(T)


def test():
    s = Solution1()
    assert s.backspaceCompare("ab#c", "ad#c") is True
    assert s.backspaceCompare("ab##", "c#d#") is True
    assert s.backspaceCompare("a##c", "#a#c") is True
    assert s.backspaceCompare("a#c", "b") is False
