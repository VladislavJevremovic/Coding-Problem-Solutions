# https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, s: str) -> str:
        """Shift each uppercase character by the A-to-a code-point offset,
        leaving everything else unchanged."""
        # Time: O(n)   Space: O(n)
        result = []
        diff = ord("A") - ord("a")
        for c in s:
            if ord("A") <= ord(c) <= ord("Z"):
                result.append(chr(ord(c) - diff))
            else:
                result.append(c)

        return "".join(result)


def test():
    s = Solution()
    assert s.toLowerCase("Hello") == "hello"
    assert s.toLowerCase("here") == "here"
    assert s.toLowerCase("LOVELY") == "lovely"
