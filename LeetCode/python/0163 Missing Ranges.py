# https://leetcode.com/problems/missing-ranges/

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """Walk the sorted numbers tracking the previous value; whenever there is
        a gap before the current number, emit the missing range."""

        # Time: O(n)   Space: O(1) excluding output
        def formatRange(lower: int, upper: int):
            if lower == upper:
                return str(lower)

            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))

            prev = curr

        return result


def test():
    s = Solution()
    assert s.findMissingRanges([0, 1, 3, 50, 75], 0, 99) == [
        "2",
        "4->49",
        "51->74",
        "76->99",
    ]
    assert s.findMissingRanges([], 1, 1) == ["1"]
    assert s.findMissingRanges([], -3, -1) == ["-3->-1"]
    assert s.findMissingRanges([-1], -1, -1) == []
    assert s.findMissingRanges([-1], -2, -1) == ["-2"]
