# https://leetcode.com/problems/first-unique-character-in-a-string/

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
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
