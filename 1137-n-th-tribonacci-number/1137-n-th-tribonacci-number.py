class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def tri(i):
            if i not in memo.keys():
                memo[i] = tri(i-1) + tri(i-2) + tri(i-3)
            
            return memo[i]
        
        return tri(n)