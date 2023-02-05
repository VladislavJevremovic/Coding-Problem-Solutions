# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        result = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1

        return result


def test():
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert s.partitionLabels("eccbbbbdec") == [10]
