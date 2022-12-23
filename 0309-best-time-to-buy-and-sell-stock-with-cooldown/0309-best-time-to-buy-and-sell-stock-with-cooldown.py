class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n+2)] # buy, sell
        
        for i in range(n-1, -1, -1):
            dp[i][0] = max(dp[i+1][0], -prices[i] + dp[i+1][1])
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+2][0])
            
        return dp[0][0]