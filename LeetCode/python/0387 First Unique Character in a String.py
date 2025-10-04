# https://leetcode.com/problems/first-unique-character-in-a-string/

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Count every character, then return the index of the first one whose
        total count is exactly one."""
        # Time: O(n)   Space: O(1) bounded alphabet
        counts = collections.defaultdict(int)
        for char in list(s):
            counts[char] += 1

        for i, char in enumerate(s):
            if counts[char] == 1:
                return i

        return -1


def test():
    s = Solution()
    assert s.firstUniqChar("leetcode") == 0
    assert s.firstUniqChar("loveleetcode") == 2
