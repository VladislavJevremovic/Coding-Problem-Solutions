# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str, low: int, high: int):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1

            return True

        def backtrack(start: int, result: List[List[str]], current: List[str], s: str):
            if start >= len(s):
                result.append(current[:])

            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    current.append(s[start:end + 1])
                    backtrack(end + 1, result, current, s)  # continue with rest of s (after 1st substring)
                    current.pop()

        result = []
        backtrack(0, result, [], s)

        return result


def test():
    s = Solution()
    assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert s.partition("a") == [["a"]]
