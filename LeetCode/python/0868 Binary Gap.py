# https://leetcode.com/problems/binary-gap/

class Solution1:
    def binaryGap(self, N: int) -> int:
        current_longest_gap = 0
        longest_gap = 0
        gap_open = False

        while N > 0:
            d = N % 2
            N //= 2

            if d == 1:
                if not gap_open:
                    gap_open = True
                else:
                    current_longest_gap += 1

                longest_gap = max(current_longest_gap, longest_gap)
                current_longest_gap = 0
            else:
                if gap_open:
                    current_longest_gap += 1

        return longest_gap


class Solution2:
    def binaryGap(self, N: int) -> int:
        last = -1
        r = 0
        for i in range(32):
            if ((N >> i) & 1) > 0:
                if last >= 0:
                    r = max(r, i - last)
                last = i

        return r


def test():
    s = Solution1()
    assert s.binaryGap(22) == 2
    assert s.binaryGap(5) == 2
    assert s.binaryGap(6) == 1
    assert s.binaryGap(8) == 0
    assert s.binaryGap(1) == 0
