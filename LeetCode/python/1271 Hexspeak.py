# https://leetcode.com/problems/hexspeak/


class Solution:
    def toHexspeak(self, num: str) -> str:
        """Convert to uppercase hex, map 0->O and 1->I, and reject any digit that
        is not a valid hexspeak letter."""
        # Time: O(d)   Space: O(d)
        h = format(int(num), "x")
        h = list(h.upper())
        s = {"A", "B", "C", "D", "E", "F", "I", "O"}
        for i in range(len(h)):
            if h[i] == "0":
                h[i] = "O"
            if h[i] == "1":
                h[i] = "I"
            if h[i] not in s:
                return "ERROR"

        return "".join(h)


def test():
    s = Solution()
    assert s.toHexspeak("257") == "IOI"
    assert s.toHexspeak("3") == "ERROR"
