# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)


def test():
    s = Solution()
    assert s.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert s.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
