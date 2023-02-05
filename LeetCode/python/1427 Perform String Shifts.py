# https://leetcode.com/problems/perform-string-shifts/

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        list_s = list(s)

        left_shift = 0
        for a_shift in shift:
            left_shift += a_shift[1] if not a_shift[0] else -a_shift[1]
        left_shift = left_shift % len(list_s)

        return "".join(list_s[left_shift:] + list_s[:left_shift])


def test():
    s = Solution()
    assert s.stringShift("abc", [[0, 1], [1, 2]]) == "cab"
    assert s.stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]) == "efgabcd"
