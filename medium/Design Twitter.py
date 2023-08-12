# https://leetcode.com/problems/design-twitter/description/
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = {}  # list; [time, tweetId]
        self.followMap = {}  # set() (followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap.keys():
            self.tweetMap[userId] = []

        self.tweetMap[userId].append([self.time, tweetId])

        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        if userId not in self.followMap.keys():
            self.followMap[userId] = set()

        self.followMap[userId].add(userId)

        for user in self.followMap[userId]:
            if user in self.tweetMap.keys():
                for tweet in self.tweetMap[user]:
                    heapq.heappush(maxHeap, tweet)

        while maxHeap and len(res) < 10:
            res.append(heapq.heappop(maxHeap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap.keys():
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)