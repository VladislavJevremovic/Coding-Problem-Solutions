# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """Count occurrences in the stones for each jewel type and sum them
        (n = stones length, k = jewel types)."""
        # Time: O(n * k)   Space: O(1)
        return sum([S.count(i) for i in J])


def test():
    s = Solution()
    assert s.numJewelsInStones("aA", "aAAbbbb") == 3
    assert s.numJewelsInStones("z", "ZZ") == 0
