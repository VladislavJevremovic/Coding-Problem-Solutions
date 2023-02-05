# https://leetcode.com/problems/counting-elements/

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in hash_set:
                count += 1

        return count


def test():
    s = Solution()
    assert s.countElements([1, 2, 3]) == 2
    assert s.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert s.countElements([1, 3, 2, 3, 5, 0]) == 3
    assert s.countElements([1, 1, 2, 2]) == 2
    assert s.countElements([1, 1, 2]) == 2
