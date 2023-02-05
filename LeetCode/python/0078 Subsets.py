# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, current=[]):
            if len(current) == k:
                result.append(current[:])  # copy
                return

            for i in range(first, n):
                current.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, current)
                current.pop()

        result = []
        n = len(nums)
        for k in range(n + 1):  # all set lengths, 0 to n
            backtrack()

        return result


def test():
    s = Solution()
    assert sorted(s.subsets([1, 2, 3]), key=lambda x: len(x)) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(s.subsets([0])) == [[], [0]]
