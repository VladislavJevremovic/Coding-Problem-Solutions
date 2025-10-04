# Conventions

How solutions in this repo are structured, documented, tested, and formatted.
See [README.md](README.md) for the high-level layout and [INDEX.md](INDEX.md)
for the full problem catalog.

## File layout

| Platform | Path | Entry point |
| --- | --- | --- |
| LeetCode | `LeetCode/python/NNNN Title.py` (flat, zero-padded number) | `class Solution` with the platform's camelCase method name |
| HackerRank | `HackerRank/<Track>/<Category>/<Problem>/Solution.py` | module-level `snake_case` function |
| Codility | `Codility/<NN. Lesson>/<Problem>/Solution.py` | `def solution(...)` |

The structural difference between platforms is intentional — each mirrors the
shape that platform expects, so a solution can be pasted back with minimal edits.
Shared linked-list / tree node types and builders live in
[`LeetCode/python/Helpers`](LeetCode/python/Helpers); LeetCode data-structure
problems import from it, while HackerRank/Codility files are self-contained.

## Anatomy of a solution file

```python
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Map each value to its index; for every number check whether its
        complement has already been seen."""
        # Time: O(n)   Space: O(n)
        ...


def test():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
```

1. **Header comment** — the problem URL. (HackerRank also keeps a
   `# HackerRank: <Name>` line; its URLs are best-effort and may not resolve.)
   Codility keeps its difficulty tag (`# Painless`, etc.).
2. **Docstring** — one line on the primary method/function describing the
   *approach*, not restating the problem. Design/multi-method classes get a
   class-level docstring.
3. **Complexity** — a `# Time: O(...)   Space: O(...)` comment immediately below
   the docstring, derived from the actual code. Multiple `Solution1`/`Solution2`
   classes are each documented and annotated separately.
4. **`test()`** — a module-level function of `assert` statements (no stdin, no
   printing at import time). Tree/linked-list cases build inputs with the
   `Helpers` builders or inline node classes and assert on serialized output.

## Running checks

```bash
pip install pytest ruff
pytest                       # full suite (importlib mode; see pyproject.toml)
ruff check .                 # lint
ruff format .                # format
python3 scripts/generate_index.py   # regenerate INDEX.md
```

Lint/format rules live in [`pyproject.toml`](pyproject.toml) (`target-version`
py39, line length 88; `E741`/`E501` are ignored for competitive-style naming).

## Adding a new solution

1. Place the file at the platform path above, with the header + docstring +
   complexity + `test()`.
2. `pytest "<path to file>"` to confirm it passes, then `ruff check`/`ruff format`.
3. `python3 scripts/generate_index.py` to refresh the catalog.

## Notes

- **SQL** solutions (`LeetCode/sql/`) are kept for reference but are **not** run
  by the suite — there is no database to execute them against.
