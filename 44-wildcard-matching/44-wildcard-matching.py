class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(index1=0, index2=0):
            if index1 >= len(s) and index2 >= len(p):
                return True
            
            if index2 >= len(p):
                return False
            
            if index1 >= len(s):
                for i in range(index2, len(p)):
                    if p[i] != "*":
                        return False
                return True
            
            
            if p[index2] == '*':
                return dp(index1+1, index2) or dp(index1, index2+1) or dp(index1+1,index2+1)
            
            if p[index2] == s[index1] or p[index2] == '?':
                return dp(index1+1, index2+1)

            
            return False
            
        return dp()