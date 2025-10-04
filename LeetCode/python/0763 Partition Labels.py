# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """Record each character's last index, then greedily close a part once
        the scan reaches the farthest last-index seen so far."""
        # Time: O(n)   Space: O(1)
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
