class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                remaining = i-coin
                if remaining >= 0:
                    dp[i] = min(dp[i], 1+dp[remaining])
        return dp[-1] if dp[-1] != float("inf") else -1
        