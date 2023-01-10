class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        @lru_cache(None)
        def rec(index, prev = None):
            if index > n:
                return float("inf")
            if index == n:
                return 0
            
            if prev == None:
                return 2 + rec(index+1, 1)
            else:
                option1 = 1 + rec(index+prev, prev)
                option2 = 2 + rec(index*2, index)
                return min(option1, option2)
        
        return rec(1)