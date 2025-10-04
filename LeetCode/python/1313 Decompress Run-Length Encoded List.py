# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """Walk the pairs (freq, val) and append val repeated freq times."""
        # Time: O(n + sum of freqs)   Space: O(sum of freqs)
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])

        return result


def test():
    s = Solution()
    assert s.decompressRLElist([1, 2, 3, 4]) == [2, 4, 4, 4]
    assert s.decompressRLElist([1, 1, 2, 3]) == [1, 3, 3]
