# https://leetcode.com/problems/top-k-frequent-words/

import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Count words, then pop k times from a heap keyed by (-frequency, word)
        so ties break lexicographically."""
        # Time: O(n + k log n)   Space: O(n)
        counts = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counts.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


def test():
    s = Solution()
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert s.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]
