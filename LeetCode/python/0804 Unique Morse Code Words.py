# https://leetcode.com/problems/unique-morse-code-words/

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        s = set()
        for word in words:
            morse_c_list = [m[ord(c) - ord("a")] for c in word]
            word = "".join(morse_c_list)
            s.add(word)

        return len(s)


def test():
    s = Solution()
    assert s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
    assert s.uniqueMorseRepresentations(["a"]) == 1
