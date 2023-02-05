# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index=0, current_subset=[]):
            result.append(current_subset[::])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue  # skip duplicates

                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        nums.sort()
        result = []
        backtrack()

        return result


def test():
    s = Solution()

    assert s.subsetsWithDup([1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert s.subsetsWithDup([0]) == [[], [0]]
