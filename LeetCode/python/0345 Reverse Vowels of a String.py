# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str) -> bool:
            return c in "aeiouAEIOU"

        n = len(s)
        if n <= 1:
            return s

        r = list(s)

        i, j = 0, n - 1
        while i < j:
            a = r[i]
            b = r[j]

            if not isVowel(a):
                i += 1
                continue

            if not isVowel(b):
                j -= 1
                continue

            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)


def test():
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"
