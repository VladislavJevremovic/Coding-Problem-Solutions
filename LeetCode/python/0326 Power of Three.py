# https://leetcode.com/problems/power-of-three/


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        """A positive n is a power of three iff it divides the largest 32-bit
        power of three, since 3 is prime."""
        # Time: O(1)   Space: O(1)
        # The biggest power of 3 that fits into 32 bits is 3486784401 (3^20).
        # For signed 32 bits it is 1162261467 (3^19):
        # 3^floor(log_3 MAX) == pow(3, floor(log(MAX) / log(3)))

        return n > 0 and not 1162261467 % n


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        """Recursively divide by 3 while divisible; a power of three reduces to 1."""
        # Time: O(log n)   Space: O(log n)
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False


def test():
    s = Solution1()
    assert s.isPowerOfThree(27) is True
    assert s.isPowerOfThree(0) is False
    assert s.isPowerOfThree(9) is True
    assert s.isPowerOfThree(45) is False
    assert s.isPowerOfThree(-3) is False
