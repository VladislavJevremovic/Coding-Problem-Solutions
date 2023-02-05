# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0
        for i in range(1, n + 1):
            result = (result + k) % i  # (f(n - 1) + k) % n

        return result + 1


def test():
    s = Solution()
    assert s.findTheWinner(5, 2) == 3
    assert s.findTheWinner(6, 5) == 1
