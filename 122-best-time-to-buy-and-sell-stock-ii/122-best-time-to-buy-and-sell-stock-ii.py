class Solution:
    def maxProfit(self, prices: List[int]) -> int:\
        
        profit = 0
        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[i-1]
            if current_profit > 0:
                profit += current_profit
        
        return profit