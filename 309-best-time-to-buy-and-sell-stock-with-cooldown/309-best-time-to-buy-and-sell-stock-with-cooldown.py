class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def getProfit(index, hasStock=False, isCooling=False):
            if index == len(prices):
                return 0
            skip = getProfit(index+1, hasStock, False )
            if isCooling:
                buy_sell = 0
            else:
                if hasStock:
                    buy_sell = getProfit(index + 1, False, True) + prices[index]
                else:
                    buy_sell = getProfit(index + 1, True, False) - prices[index]
            return max(buy_sell, skip)
        
        return getProfit(0)