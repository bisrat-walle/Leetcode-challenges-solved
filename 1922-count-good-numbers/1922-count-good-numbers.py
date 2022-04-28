class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        fours = n // 2
        fives = (n + 1) // 2
        mod = 10**9 + 7
        
        ans = pow(4, fours, mod) * pow(5, fives, mod)
        return ans % mod