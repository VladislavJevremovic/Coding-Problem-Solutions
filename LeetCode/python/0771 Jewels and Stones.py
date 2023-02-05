# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(i) for i in J])


def test():
    s = Solution()
    assert s.numJewelsInStones("aA", "aAAbbbb") == 3
    assert s.numJewelsInStones("z", "ZZ") == 0
