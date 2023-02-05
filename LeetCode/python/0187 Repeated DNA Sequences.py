# https://leetcode.com/problems/repeated-dna-sequences/

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, result = set(), set()

        for start in range(n - L + 1):  # all sequences of length L
            t = s[start:start + L]
            if t in seen:
                result.add(t[:])
            seen.add(t)

        return list(result)


def test():
    s = Solution()
    assert sorted(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == \
           sorted(["AAAAACCCCC", "CCCCCAAAAA"])
    assert sorted(s.findRepeatedDnaSequences("AAAAAAAAAAAAA")) == sorted(["AAAAAAAAAA"])
