# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# HackerRank: Designer PDF Viewer
from typing import List


def designer_pdf_viewer(h: List[int], word: str) -> int:
    """Highlight area is the tallest letter height times the word length."""
    # Time: O(L)   Space: O(1)  (L = word length)
    tallest = max(h[ord(c) - ord("a")] for c in word)
    return tallest * len(word)


def test() -> None:
    heights = [
        1,
        3,
        1,
        3,
        1,
        4,
        1,
        3,
        2,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        7,
    ]
    assert designer_pdf_viewer(heights, "abc") == 9
    assert designer_pdf_viewer(heights, "zaba") == 28
