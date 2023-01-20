class Twitter:

    def __init__(self):
        self.followee = defaultdict(set)
        self.tweets = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for item in self.tweets[userId]:
            heappush(feed, item)
            if len(feed) > 10:
                heappop(feed)
            
        for user in self.followee[userId]:
            for item in self.tweets[user]:
                heappush(feed, item)
                if len(feed) > 10:
                    heappop(feed)
        
        ans = []
        
        while feed:
            ans.append(heappop(feed)[1])
        
        ans.reverse()
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)