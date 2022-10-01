class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = dict(zip(map(str, range(1, 27)), map(lambda k:chr(k+64), range(1, 27))))
        dp = [0 for i in range(len(s)+1)]
        dp[len(s)] = 1
        for i in reversed(range(len(s))):
            if i != len(s)-1:
                if s[i:i+2] in mapping:
                    dp[i] += dp[i+2]
            if s[i] in mapping:
                dp[i] += dp[i+1]
        return dp[0]