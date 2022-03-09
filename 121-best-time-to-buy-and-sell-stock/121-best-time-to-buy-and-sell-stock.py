class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        left_ptr = 0
        right_ptr = 1 
        max_profit = 0
        
        while right_ptr < n:
            
            current_profit = prices[right_ptr] - prices[left_ptr] 
            
            if prices[left_ptr] < prices[right_ptr]:
                max_profit =max(current_profit,max_profit)
            else:
                left_ptr = right_ptr
            right_ptr += 1
        return max_profit
            
        
        