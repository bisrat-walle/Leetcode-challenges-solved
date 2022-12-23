class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def rec(index, canBuy=True):
            if index >= n:
                return 0
            option1 = rec(index+1, canBuy)
            if canBuy:
                option2 = -prices[index] + rec(index+1, False)
            else:
                option2 = prices[index] + rec(index+2, True)
            
            return max(option1, option2)
        
        return rec(0)