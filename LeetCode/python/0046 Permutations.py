# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        self.permutation(nums, [], result)

        return result

    def permutation(self, nums: List[int], current, result: List[List[int]]) -> None:
        if not nums:
            result.append(current)
            return

        for i in range(len(nums)):
            self.permutation(nums[:i] + nums[(i + 1):], current + [nums[i]], result)


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                # place i-th num first in current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next nums to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()

        return output


def test():
    s = Solution()
    assert s.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert s.permute([0, 1]) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]
