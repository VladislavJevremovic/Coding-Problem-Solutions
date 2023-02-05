# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []

        # a = 0
        # b = n
        # while a < n:
        #     r.append(nums[a])
        #     r.append(nums[b])
        #     a += 1
        #     b += 1

        a = nums[:n]
        b = nums[n:]
        for i in range(len(a)):
            r.append(a[i])
            r.append(b[i])

        return r


def test():
    s = Solution()
    assert s.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert s.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
    assert s.shuffle([1, 2], 1) == [1, 2]
