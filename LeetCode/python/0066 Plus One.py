# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for digit in reversed(digits):
            sum = digit + carry
            result.append(sum % 10)
            carry = sum // 10

        if carry > 0:
            result.append(carry)

        return list(reversed(result))


def test():
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
