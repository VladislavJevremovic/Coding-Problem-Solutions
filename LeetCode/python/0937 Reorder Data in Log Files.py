# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            ident, rest = log.split(" ", 1)
            return (0, rest, ident) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)


def test():
    s = Solution()
    assert s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]) == \
           ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    assert s.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]) == \
           ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
