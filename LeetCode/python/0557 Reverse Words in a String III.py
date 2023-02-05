# https://leetcode.com/problems/reverse-words-in-a-string-iii/

from typing import List


class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])


class Solution2:
    def reverseWords(self, s: str) -> str:
        def reverse(s: List[str], i: int, j: int):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        list_s = list(s)
        i = 0
        word_start = 0
        while i < len(list_s):
            if s[i] == ' ':
                reverse(list_s, word_start, i - 1)
                word_start = i + 1

            i += 1
        reverse(list_s, word_start, i - 1)

        return ''.join(list_s)


def test():
    s = Solution2()  # Solution1()
    assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert s.reverseWords("God Ding") == "doG gniD"
