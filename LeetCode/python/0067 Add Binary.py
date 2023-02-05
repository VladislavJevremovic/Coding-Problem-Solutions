# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = ""
        c = 0
        pa = len(a) - 1
        pb = len(b) - 1
        while pa >= 0 or pb >= 0:
            if pa >= 0:
                c += int(a[pa])
                pa -= 1
            if pb >= 0:
                c += int(b[pb])
                pb -= 1

            r = str(c % 2) + r
            c //= 2

        if c:
            r = str(c) + r

        return r


def test():
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("0", "1") == "1"
    assert s.addBinary("1", "0") == "1"
    assert s.addBinary("1", "1") == "10"
