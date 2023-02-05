# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()

        return output


def test():
    s = Solution()
    assert sorted(s.combine(4, 2)) == sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
    assert sorted(s.combine(1, 1)) == sorted([[1]])
