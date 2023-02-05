# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue

            if c == "(":
                stack.append(i)
            elif not stack:  # ")", empty stack
                indexes_to_remove.add(i)
            else:  # ")", non-empty stack
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)

        return "".join(string_builder)


def test():
    s = Solution()
    assert s.minRemoveToMakeValid("lee(t(c)o)de)") in ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]
    assert s.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert s.minRemoveToMakeValid("))((") == ""
    assert s.minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"
