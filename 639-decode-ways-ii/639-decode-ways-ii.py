class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = dict(zip(map(str, range(1, 27)), [1]*26))
        mapping["1*"] = 9
        mapping["2*"] = 6
        mapping["*"] = 9
        mapping["**"] = 15
        dp = [0]*(len(s)+1)
        dp[len(s)] = 1
        dp[len(s)-1] = mapping[s[len(s)-1]] if s[len(s)-1] != "0" else 0
        mod = 10**9+7
        for i in reversed(range(len(s)-1)):
            if s[i] in mapping:
                dp[i] += (mapping[s[i]]*dp[i+1])%mod
            if i < len(s)-1:
                key = s[i:i+2]
                if key in mapping:
                    dp[i] += (mapping[key]*dp[i+2])%mod
                elif s[i] == "*":
                    if s[i+1] <= "6":
                        dp[i] += (2*dp[i+2])%mod
                    else:
                        dp[i] += dp[i+2]%mod
        return dp[0]%(mod)
                    
                