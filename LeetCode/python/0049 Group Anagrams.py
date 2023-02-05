# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

from python.Helpers.Functions import sorted_list_of_lists


class Solution1:  # O(NKlogK), O(NK)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))  # e.g. ('a', 'e', 't')
            result[key].append(s)

        return list(result.values())


class Solution2:  # O(NK), O(NK)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def character_count(s: str) -> List[int]:
            result = [0] * 26
            for c in s:
                result[ord(c) - ord('a')] += 1

            return result

        result = defaultdict(list)
        for s in strs:
            key = tuple(character_count(s))
            result[key].append(s)

        return list(result.values())


def test():
    def case(strs: List[str], expected: List[List[str]]) -> bool:
        return sorted_list_of_lists(Solution2().groupAnagrams(strs)) == sorted_list_of_lists(expected)

    assert case(["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert case([""], [[""]])
    assert case(["a"], [["a"]])
