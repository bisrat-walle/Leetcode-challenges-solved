class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = dict(zip(map(str, range(1, 27)), map(lambda k:chr(k+64), range(1, 27))))
        cache = {}
        def rec(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return 1
            ans = 0
            
            option1 = s[i]
            if i < len(s)-1:
                option2 = s[i:i+2]
                if option2 in mapping:
                    ans += rec(i+2)
            if option1 in mapping:
                ans += rec(i+1)
            cache[i] = ans
            return cache[i]
        return rec(0)