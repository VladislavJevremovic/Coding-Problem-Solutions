# https://app.codility.com/programmers/lessons/99-future_training/tree_height/
# Painless

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Tree:
    x: int = 0
    l: Optional["Tree"] = None
    r: Optional["Tree"] = None


def solution(T: Optional[Tree]) -> int:
    """Recurse into both children and return one plus the taller subtree's height (empty tree is -1)."""
    # Time: O(n)   Space: O(h)
    if T is None:
        return -1

    return max(solution(T.l), solution(T.r)) + 1


def test() -> None:
    assert solution(None) == -1
    assert solution(Tree()) == 0
    assert solution(Tree(l=Tree(), r=Tree())) == 1
    # Skewed tree of depth 3
    assert solution(Tree(l=Tree(l=Tree(l=Tree())))) == 3
