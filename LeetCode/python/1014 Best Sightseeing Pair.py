# https://leetcode.com/problems/best-sightseeing-pair/

import math
from typing import List


# A[i] + i + A[j] - j

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0]  # + (i=)0
        result = -math.inf
        for i in range(1, len(values)):
            result = max(result, left + values[i] - i)
            left = max(left, values[i] + i)

        return result


def test():
    s = Solution()
    assert s.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert s.maxScoreSightseeingPair([1, 2]) == 2
