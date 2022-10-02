class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def rec(current, n):
            if current == 0 and n == 0:
                return 1
            if n == 0:
                return 0
            ans = 0
            for i in range(1, k+1):
                ans = (ans%mod + rec(current-i, n-1)%mod)%mod
            return ans
        
        return rec(target, n)