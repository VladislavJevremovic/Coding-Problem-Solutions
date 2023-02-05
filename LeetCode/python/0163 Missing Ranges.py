# https://leetcode.com/problems/missing-ranges/

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower: int, upper: int):
            if lower == upper:
                return str(lower)

            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper + 1

            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))

            prev = curr

        return result


def test():
    s = Solution()
    assert s.findMissingRanges([0, 1, 3, 50, 75], 0, 99) == ["2", "4->49", "51->74", "76->99"]
    assert s.findMissingRanges([], 1, 1) == ["1"]
    assert s.findMissingRanges([], -3, -1) == ["-3->-1"]
    assert s.findMissingRanges([-1], -1, -1) == []
    assert s.findMissingRanges([-1], -2, -1) == ["-2"]
