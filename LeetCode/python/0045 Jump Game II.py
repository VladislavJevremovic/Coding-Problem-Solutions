# https://leetcode.com/problems/jump-game-ii/solution/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # if end of the current jump, need another one
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps


def test():
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
