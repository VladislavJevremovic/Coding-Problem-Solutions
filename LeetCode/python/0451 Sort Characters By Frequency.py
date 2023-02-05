# https://leetcode.com/problems/sort-characters-by-frequency/

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)

        string_builder = []
        for letter, freq in counts.most_common():
            string_builder.append(letter * freq)

        return "".join(string_builder)


def test():
    s = Solution()
    assert s.frequencySort("tree") in ["eert", "eetr"]
    assert s.frequencySort("cccaaa") in ["aaaccc", "cccaaa"]
    assert s.frequencySort("Aabb") in ["bbAa", "bbaA"]
