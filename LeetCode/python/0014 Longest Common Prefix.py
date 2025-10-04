# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Compare characters column by column against the first string, stopping
        at the first mismatch or end of any string."""
        # Time: O(n * m) for n strings of min length m   Space: O(m)
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        r = []  # resulting prefix character array
        i = 0  # resulting prefix length
        while True:
            if len(strs[0]) == i:  # it can't get any longer
                return "".join(r)

            c = strs[0][i]  # fix one, check against others
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != c:
                    return "".join(r)

            i += 1
            r.append(c)


def test():
    s = Solution()
    assert s.longestCommonPrefix([]) == ""
    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["a"]) == "a"
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
