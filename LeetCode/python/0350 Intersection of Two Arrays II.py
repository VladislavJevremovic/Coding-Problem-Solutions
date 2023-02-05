# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        r = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                r.append(nums1[i])
                i += 1
                j += 1

        return r


def test():
    s = Solution()
    assert sorted(s.intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
    assert sorted(s.intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
