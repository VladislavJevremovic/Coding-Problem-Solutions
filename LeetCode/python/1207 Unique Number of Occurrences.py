# https://leetcode.com/problems/unique-number-of-occurrences

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """Count occurrences, then check the count values are all distinct by
        comparing set size to dict size."""
        # Time: O(n)   Space: O(n)
        counts = {}
        for n in arr:
            if n not in counts:
                counts[n] = 0
            else:
                counts[n] += 1

        return len(set(counts.values())) == len(counts)


def test():
    s = Solution()
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
    assert s.uniqueOccurrences([1, 2]) is False
    assert s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True
