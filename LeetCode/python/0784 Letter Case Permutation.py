# https://leetcode.com/problems/letter-case-permutation/

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        r = [[]]
        for c in s:
            n = len(r)
            if c.isalpha():
                for i in range(n):
                    r.append(r[i][:])  # duplicate words
                    r[i].append(c.lower())  # add lower(c) to each word in first half
                    r[n + i].append(c.upper())  # add upper(c) to each word in second half
            else:
                for i in range(n):
                    r[i].append(c)  # add digits to each word

        return list(map("".join, r))


def test():
    s = Solution()
    assert sorted(s.letterCasePermutation("a1b2")) == sorted(["a1b2", "a1B2", "A1b2", "A1B2"])
    assert sorted(s.letterCasePermutation("3z4")) == sorted(["3z4", "3Z4"])
    assert sorted(s.letterCasePermutation("12345")) == sorted(["12345"])
    assert sorted(s.letterCasePermutation("0")) == sorted(["0"])
