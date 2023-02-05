# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        for i in reversed(range(m + n)):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[i] = nums2[p2]
                    p2 -= 1
            elif p1 < 0 <= p2:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p1 >= 0 > p2:
                # nums1[i] = nums1[p1] # redundant
                # p1 -= 1
                break
            else:
                break


def test():
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [2, 0]
    nums2 = [1]
    s.merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 2]

    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
