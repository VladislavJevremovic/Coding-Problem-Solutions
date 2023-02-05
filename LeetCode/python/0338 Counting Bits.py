# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        r = [0]
        if num < 1:
            return r

        for i in range(1, num + 1):
            if not i % 2:
                r.append(r[i // 2])
            else:
                r.append(r[i - 1] + 1)

        return r


def test():
    s = Solution()
    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
