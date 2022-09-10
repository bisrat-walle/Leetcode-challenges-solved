class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def rec(index, transaction=0, hasStock=False):
            if index == len(prices) or transaction == k:
                return 0
            ans = rec(index+1, transaction, hasStock)
            if hasStock:
                ans = max(ans, prices[index]+rec(index+1, transaction+1, not hasStock))
            else:
                ans = max(ans, -prices[index]+rec(index+1, transaction, not hasStock))
            return ans
        return rec(0)