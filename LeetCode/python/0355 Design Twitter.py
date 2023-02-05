# https://leetcode.com/problems/design-twitter/

from collections import defaultdict
from typing import List, Optional


class Twitter:
    def __init__(self):
        self.followed_users = defaultdict(set)  # userId: (followeeId)
        self.tweets = defaultdict(list)  # userId: [tweetId]

        self.tweet_count = 1
        self.tweet_order = dict()  # tweetId: tweet_count

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)

        self.tweet_order[tweetId] = self.tweet_count
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followed_users[userId].add(userId)

        tweets = []
        for f in self.followed_users[userId]:
            tweets += self.tweets[f]

        return sorted(tweets, key=lambda x: -self.tweet_order[x])[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed_users[followerId]:
            self.followed_users[followerId].remove(followeeId)


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "Twitter":
                s = Twitter()
                actual.append(None)
            elif action == "postTweet":
                s.postTweet(param[0], param[1])
                actual.append(None)
            elif action == "getNewsFeed":
                actual.append(s.getNewsFeed(param[0]))
            elif action == "follow":
                s.follow(param[0], param[1])
                actual.append(None)
            elif action == "unfollow":
                s.unfollow(param[0], param[1])
                actual.append(None)

        return actual == expected

    assert case(
        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
        [None, None, [5], None, None, [6, 5], None, [5]]
    )
