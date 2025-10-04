# https://leetcode.com/problems/permutations-ii/

from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Backtrack over distinct values using a frequency counter, so each
        duplicate is placed only as many times as it occurs."""

        # Time: O(n * n!)   Space: O(n) recursion depth (plus output)
        def backtrack(combination=None, counter=None):
            if combination is None:
                combination = []
            if len(combination) == len(nums):
                results.append(combination[:])
                return

            for num in counter:
                if counter[num] > 0:
                    combination.append(num)
                    counter[num] -= 1

                    backtrack(combination, counter)

                    combination.pop()
                    counter[num] += 1

        results = []
        backtrack([], Counter(nums))

        return results


def test():
    s = Solution()
    assert s.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert s.permuteUnique([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
