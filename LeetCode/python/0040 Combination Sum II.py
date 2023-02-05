# https://leetcode.com/problems/combination-sum-ii/

from collections import Counter
from typing import List

from python.Helpers.Functions import sorted_list_of_lists


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(combination, remainder, current, counter, result):
            if remainder == 0:
                result.append(combination[:])
                return
            elif remainder < 0:
                return

            for next_current in range(current, len(counter)):
                candidate, freq = counter[next_current]
                if freq <= 0:
                    continue

                combination.append(candidate)
                counter[next_current] = (candidate, freq - 1)

                backtrack(combination, remainder - candidate, next_current, counter, result)

                combination.pop()
                counter[next_current] = (candidate, freq)

        result = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]

        backtrack([], target, 0, counter, result)

        return result


def test():
    def case(candidates: List[int], target: int, expected: List[List[int]]) -> bool:
        return sorted_list_of_lists(Solution().combinationSum2(candidates, target)) == sorted_list_of_lists(expected)

    assert case([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    assert case([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]])
