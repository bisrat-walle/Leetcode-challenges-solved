class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7
        dp = [[0 for i in range(n+1)] for j in range(target+1)]
        dp[0][0] = 1
        
        for i in range(1, target+1):
            for j in range(1, n+1):
                for k in range(1, k+1):
                    if i-k > -1:
                        dp[i][j] = (dp[i][j]%mod + dp[i-k][j-1]%mod)%mod
                
# Top down        
#         @lru_cache(None)
#         def rec(current, n):
#             if current == 0 and n == 0:
#                 return 1
#             if n == 0:
#                 return 0
#             ans = 0
#             for i in range(1, k+1):
#                 ans = (ans%mod + rec(current-i, n-1)%mod)%mod
#             return ans
        
        return dp[target][n]