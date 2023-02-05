# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        for r in range(2, n + 1):
            for k in range(1, r + 1):
                f[r] += f[k - 1] * f[r - k]

        return f[n]


def test():
    s = Solution()
    assert s.numTrees(3) == 5
