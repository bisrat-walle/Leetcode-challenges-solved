class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = defaultdict(int)
        ans = 0
        for t in time:
            rem = t % 60
            ans += counter[(60 - rem) % 60]
            counter[rem] += 1
            # print(counter, f"{t},{rem}", ans)
        return ans