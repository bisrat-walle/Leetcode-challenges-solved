class Solution:
    def countPalindromes(self, s: str) -> int:
        
        n = len(s)
        mod = 10**9 + 7
        ans = 0
        
        for a in range(10):
            for b in range(10):
                
                pattern = f"?{a}{b}*{b}{a}"
                
                dp = [0 for i in range(6)]
                dp[0] = 1
                
                for i in range(n):
                    for j in reversed(range(1, 6)):
                        if j == 3 or s[i] == pattern[j]:
                            dp[j] += dp[j-1]
                # print(pattern, dp)
                ans += dp[-1]%mod 
        
        return ans%mod