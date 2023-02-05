# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            result.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            result.append(carry)

        return ''.join(str(x) for x in result[::-1])


def test():
    s = Solution()
    assert s.addStrings("11", "123") == "134"
    assert s.addStrings("456", "77") == "533"
    assert s.addStrings("0", "0") == "0"
