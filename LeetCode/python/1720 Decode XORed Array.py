# https://leetcode.com/problems/decode-xored-array/

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = [first]
        for i in range(len(encoded)):
            r.append(encoded[i] ^ r[i])

        return r


def test():
    s = Solution()
    assert s.decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert s.decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
