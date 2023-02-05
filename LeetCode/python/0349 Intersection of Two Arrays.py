# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        r = []
        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]
            if a < b:
                i += 1
            elif a > b:
                j += 1
            else:
                r.append(a)
                while i < len(nums1) and nums1[i] == a:
                    i += 1
                while j < len(nums2) and nums2[j] == b:
                    j += 1

        return r


def test():
    s = Solution()
    assert sorted(s.intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(s.intersection([2, 2], [1, 2, 2, 1])) == [2]
    assert sorted(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert sorted(s.intersection([9, 4, 9, 8, 4], [4, 9, 5])) == [4, 9]
