# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            num = num - 1 if num % 2 else num // 2
            steps += 1

        return steps


def test():
    s = Solution()
    assert s.numberOfSteps(14) == 6
    assert s.numberOfSteps(8) == 4
    assert s.numberOfSteps(123) == 12
