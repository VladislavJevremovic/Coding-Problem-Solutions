# Coding-Problem-Solutions

[![tests](https://github.com/VladislavJevremovic/Coding-Problem-Solutions/actions/workflows/tests.yml/badge.svg)](https://github.com/VladislavJevremovic/Coding-Problem-Solutions/actions/workflows/tests.yml)

My solutions to programming problems from LeetCode, HackerRank, and Codility — all in Python, each verified by an inline test.

Browse the full catalog in [INDEX.md](INDEX.md), learn the algorithmic topics and techniques behind the problems in [TOPICS.md](TOPICS.md), or see [CONVENTIONS.md](CONVENTIONS.md) for how solutions are structured.

## Layout

| Platform | Path | Solutions | Language |
| --- | --- | --- | --- |
| [LeetCode](https://leetcode.com/) | [`LeetCode/python`](LeetCode/python) | ~290 | Python |
| [LeetCode](https://leetcode.com/) (database) | [`LeetCode/sql`](LeetCode/sql) | 1 | SQL |
| [HackerRank](https://www.hackerrank.com/) | [`HackerRank`](HackerRank) | ~125 | Python |
| [Codility](https://app.codility.com/) | [`Codility`](Codility) | 24 | Python |

- **LeetCode** is a flat folder of files named `NNNN Problem Title.py` (zero-padded problem number). Shared utilities (linked-list / tree node types and builders) live in [`LeetCode/python/Helpers`](LeetCode/python/Helpers).
- **HackerRank** mirrors the site's tracks: `HackerRank/<Track>/<Category>/<Problem>/Solution.py`.
- **Codility** mirrors the lessons: `Codility/<NN. Lesson>/<Problem>/Solution.py`.

## Conventions

Every solution file is self-contained and follows the same shape:

```python
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ...


def test():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
```

- A top comment links the original problem.
- The solution is exposed as a function or class — no reading from stdin or printing at import time, so every file is importable and testable.
- A module-level `def test()` holds `assert`-based cases. Some files keep more than one approach (`Solution1`, `Solution2`, ...) and assert each against the same cases.

## Running the tests

The whole repo is one pytest suite (config in [`pyproject.toml`](pyproject.toml)):

```bash
pip install pytest
pytest                      # run everything
pytest LeetCode/python      # one platform
pytest "LeetCode/python/0001 Two Sum.py"   # one problem
```

Discovery is customized because the files are named `Solution.py` / `NNNN Title.py` and the test function is just `test()`: pytest runs in `importlib` mode with `python_files = *.py` and `python_functions = test`.

Continuous integration runs the suite on every push and pull request against Python 3.9 and 3.12 — see [`.github/workflows/tests.yml`](.github/workflows/tests.yml).

## License

[MIT](LICENSE)
