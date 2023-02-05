# https://leetcode.com/problems/reverse-words-in-a-string/

from collections import deque
from typing import List


class Solution1:
    def reverseWords(self, s: str) -> str:
        # Use built-in split and reverse.
        # Benefits: in-place in Python (in-place, but linear space complexity!) and the simplest one to write.

        return ' '.join(reversed(s.split()))


class Solution2:
    # The most straightforward one. Trim the whitespaces, reverse the whole string and then reverse each word.
    # Benefits: could be done in-place for the languages with mutable strings (not Python).

    def trim_spaces(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, list: List[str], left: int, right: int) -> None:
        while left < right:
            list[left], list[right] = list[right], list[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, list: List[str]) -> None:
        n = len(list)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and list[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(list, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # convert string to char array and trim spaces at the same time
        list = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(list, 0, len(list) - 1)

        # reverse each word
        self.reverse_each_word(list)

        return ''.join(list)


class Solution3:
    def reverseWords(self, s: str) -> str:
        # Two passes approach with a deque. 
        # Move along the string, word by word, and push each new word in front of the deque.
        # Convert the deque back into string. 
        # Benefits: two passes.

        left, right = 0, len(s) - 1

        # trim edges
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))  # add leftover

        return ' '.join(d)


def test():
    s = Solution3()
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good   example") == "example good a"
    assert s.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    assert s.reverseWords("Alice does not even like bob") == "bob like even not does Alice"
