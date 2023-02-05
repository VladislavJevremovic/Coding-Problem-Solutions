# https://leetcode.com/problems/combination-sum-iii/

from typing import List

from python.Helpers.Functions import sorted_list_of_lists


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start: int, remainder: int, current: List[int]):
            if len(current) > k or remainder < 0:
                return

            if len(current) == k and remainder == 0:
                result.append(current[:])

            for num in range(start, 10):
                current.append(num)
                backtrack(num + 1, remainder - num, current)
                current.pop()

        result = []
        backtrack(1, n, [])

        return result


def test():
    def case(k: int, n: int, expected: List[List[int]]) -> bool:
        return sorted_list_of_lists(Solution().combinationSum3(k, n)) == sorted_list_of_lists(expected)

    assert case(3, 7, [[1, 2, 4]])
    assert case(3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
    assert case(4, 1, [])
    assert case(3, 2, [])
    assert case(9, 45, [[1, 2, 3, 4, 5, 6, 7, 8, 9]])
