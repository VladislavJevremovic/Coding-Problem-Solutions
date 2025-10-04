# https://leetcode.com/problems/design-browser-history/
from typing import Any, List, Optional


class BrowserHistory:
    """Two stacks: a back stack of visited pages and a forward stack for redo."""

    def __init__(self, homepage: str):
        # Time: O(1)   Space: O(1)
        self.previous = [homepage]
        self.next = []

    def visit(self, url: str) -> None:
        # Time: O(1)   Space: O(1)
        self.previous.append(url)
        self.next = []

    def back(self, steps: int) -> str:
        # Time: O(steps)   Space: O(1)
        while steps > 0 and len(self.previous) > 1:
            self.next.append(self.previous[-1])
            self.previous.pop()
            steps -= 1

        return self.previous[-1]

    def forward(self, steps: int) -> str:
        # Time: O(steps)   Space: O(1)
        while steps > 0 and self.next:
            self.previous.append(self.next[-1])
            self.next.pop()
            steps -= 1

        return self.previous[-1]


def test():
    def case(
        actions: List[str], params: List[Any], expected: List[Optional[str]]
    ) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "BrowserHistory":
                s = BrowserHistory(param[0])
                actual.append(None)
            elif action == "visit":
                s.visit(param[0])
                actual.append(None)
            elif action == "back":
                actual.append(s.back(param[0]))
            elif action == "forward":
                actual.append(s.forward(param[0]))

        return actual == expected

    assert case(
        [
            "BrowserHistory",
            "visit",
            "visit",
            "visit",
            "back",
            "back",
            "forward",
            "visit",
            "forward",
            "back",
            "back",
        ],
        [
            ["leetcode.com"],
            ["google.com"],
            ["facebook.com"],
            ["youtube.com"],
            [1],
            [1],
            [1],
            ["linkedin.com"],
            [2],
            [2],
            [7],
        ],
        [
            None,
            None,
            None,
            None,
            "facebook.com",
            "google.com",
            "facebook.com",
            None,
            "linkedin.com",
            "google.com",
            "leetcode.com",
        ],
    )
