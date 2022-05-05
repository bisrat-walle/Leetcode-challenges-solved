class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # print(self.getString(1))
        # print(self.getString(2))
        # print(self.getString(3))
        # print(self.getString(4))
        return self.getString(n)[k-1]
    @lru_cache(None)
    def getString(self, n):
        if n==0:
            return "0"
        return self.getString(n-1)+"1"+"".join(list(reversed(self.invert(self.getString(n-1)))))
    
    def invert(self, s):
        s = [i for i in s]
        for i in range(len(s)):
            if s[i] == "0": 
                s[i] = "1"
                continue
            s[i] = "0"
        return ''.join(s)
    