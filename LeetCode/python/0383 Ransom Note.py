# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Multiset difference of Counters: the note is buildable iff subtracting
        the magazine's letters leaves nothing missing."""
        # Time: O(n + m)   Space: O(1) bounded alphabet
        # if not ransomNote:
        #     return True

        # if not magazine:
        #     return False

        # r_c = Counter(ransomNote)
        # r_m = Counter(magazine)
        # for w in r_c:
        #     if r_m[w] < r_c[w]:
        #         return False

        # return True

        return not len(
            Counter(ransomNote) - Counter(magazine)
        )  # deletes only matching pairs


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Tally the magazine's letters in a 26-slot array, subtract the note's,
        and confirm no count went negative."""
        # Time: O(n + m)   Space: O(1)
        if not ransomNote:
            return True

        if not magazine:
            return False

        d = [0] * 26

        for c in magazine:
            d[ord(c) - ord("a")] += 1

        for c in ransomNote:
            d[ord(c) - ord("a")] -= 1

        return all(c >= 0 for c in d)


def test():
    s = Solution1()
    assert s.canConstruct("", "b") is True
    assert s.canConstruct("a", "") is False
    assert s.canConstruct("a", "b") is False
    assert s.canConstruct("aa", "ab") is False
    assert s.canConstruct("aa", "aab") is True
    assert s.canConstruct("aa", "aaab") is True
