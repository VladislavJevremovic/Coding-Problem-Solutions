# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while True:
                if k == 0 or not stack:
                    break

                if stack[-1] > num[i]:
                    k -= 1  # pop larger digits
                    stack.pop()
                else:
                    break
            stack.append(num[i])

        for _ in range(k):  # pop off right remaining k times
            stack.pop()

        return "".join(stack).lstrip("0") or "0"


def test():
    s = Solution()
    assert s.removeKdigits("1432219", 3) == "1219"
    assert s.removeKdigits("10200", 1) == "200"
    assert s.removeKdigits("10", 2) == "0"
