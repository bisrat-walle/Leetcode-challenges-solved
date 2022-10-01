class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = dict(zip(map(str, range(1, 27)), [1]*26))
        mapping["1*"] = 9
        mapping["2*"] = 6
        mapping["*"] = 9
        mapping["**"] = 15
        first = 1
        second = mapping[s[len(s)-1]] if s[len(s)-1] != "0" else 0
        mod = 10**9+7
        for i in reversed(range(len(s)-1)):
            temp = 0
            if s[i] in mapping:
                temp += (mapping[s[i]]*second)%mod
            if i < len(s)-1:
                key = s[i:i+2]
                if key in mapping:
                    temp += (mapping[key]*first)%mod
                elif s[i] == "*":
                    if s[i+1] <= "6":
                        temp += (2*first)%mod
                    else:
                        temp += first%mod
            first, second = second, temp
        return second%(mod)
                    
                