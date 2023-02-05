# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n  # length of longest sequence till i-th position
        count = [1] * n  # count of longest sequence of length lis[i]
        max_len = 1  # maximum length of lis
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lis[j] + 1 > lis[i]:  # strictly increasing
                        lis[i] = lis[j] + 1
                        count[i] = count[j]
                    elif lis[j] + 1 == lis[i]:  # more same-length subsequences ending at lis[i]
                        count[i] += count[j]

            max_len = max(max_len, lis[i])

        number_of_list = 0
        for i in range(n):
            if lis[i] == max_len:
                number_of_list += count[i]

        return number_of_list


def test():
    s = Solution()
    assert s.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert s.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
