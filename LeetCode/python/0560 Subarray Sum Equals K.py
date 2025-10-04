# https://leetcode.com/problems/subarray-sum-equals-k/

import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Track prefix-sum frequencies; each running sum contributes the count
        of earlier prefixes equal to sum - k."""
        # Time: O(n)   Space: O(n)
        result, sum_to_i = 0, 0
        dict = collections.defaultdict(int)
        dict[0] = 1  # {s[i]: occurrences of s[i]}
        for num in nums:
            sum_to_i += num
            if (sum_to_i - k) in dict:
                result += dict[sum_to_i - k]  # sum_to_i − sum_to_j = k (prefix sum)
            dict[sum_to_i] = dict[sum_to_i] + 1

        return result


def test():
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
