# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remainder, combination, start):
            if remainder == 0:
                result.append(combination[:])
                return
            elif remainder < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remainder - candidates[i], combination, i)  # c[i] will be tested until r < 0
                combination.pop()

        result = []
        backtrack(target, [], 0)

        return result


def test():
    s = Solution()
    assert s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []
    assert s.combinationSum([1], 1) == [[1]]
    assert s.combinationSum([1], 2) == [[1, 1]]
