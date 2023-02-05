# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # since they're now sorted, nothing more possible

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # don't try the same, previous search

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:  # can't use the same number twice
                sum = nums[i] + nums[lo] + nums[hi]
                if sum == 0:
                    result.append([nums[i], nums[lo], nums[hi]])

                    # skip the same values
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi - 1] == nums[hi]:
                        hi -= 1

                    lo += 1
                    hi -= 1
                elif sum < 0:
                    lo += 1
                else:
                    hi -= 1

        return result


def test():
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
