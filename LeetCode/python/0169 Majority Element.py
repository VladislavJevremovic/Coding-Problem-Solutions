# https://leetcode.com/problems/majority-element/

import collections
from typing import List


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] > len(nums) // 2:
                return num

        return -1


class Solution2:  # Boyer-Moore
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count += -1

        return candidate


def test():
    s = Solution2()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
