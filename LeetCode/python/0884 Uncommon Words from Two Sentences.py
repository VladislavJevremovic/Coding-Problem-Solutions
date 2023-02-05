# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split() + B.split())

        return [word for word in c if c[word] == 1]


def test():
    s = Solution()
    assert s.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert s.uncommonFromSentences("apple apple", "banana") == ["banana"]
