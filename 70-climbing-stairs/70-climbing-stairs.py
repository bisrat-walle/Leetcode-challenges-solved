class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        def find(n):
            if n <= 2:
                return n
            if n not in dp.keys():
                dp[n] = find(n-1) + find(n-2)
                return dp[n]
            return dp[n]
        
        return find(n)
    
        