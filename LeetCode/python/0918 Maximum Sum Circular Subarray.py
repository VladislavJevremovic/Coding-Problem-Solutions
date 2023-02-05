# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List


# 1) Subarray takes only a middle part, and we know how to find the max subarray sum.
# 2) Subarray takes a part of head array and a part of tail array.

# max(max subarray sum, total sum - min subarray sum)

# Proof:
# max(prefix + suffix) = max(total sum - subarray) = total sum + max(-subarray) = total sum - min(subarray)

# If all numbers are negative, maxSum = max(A) and minSum = sum(A).
# In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
# According to the deacription, We need to return the max(A), instead of sum of an empty subarray.
# So we return the maxSum to handle this corner case.

# Complexity: O(N), O(1)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for a in nums:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


def test():
    s = Solution()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([3, -1, 2, -1]) == 4
    assert s.maxSubarraySumCircular([3, -2, 2, -3]) == 3
    assert s.maxSubarraySumCircular([-2, -3, -1]) == -1
