class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        def dp(i, j):
            if j >= len(t) and not (i >= len(s)):
                return False
            if i >= len(s):
                return True
            
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
            if (i, j) not in memo.keys():
                memo[(i, j)] = dp(i, j)
            
            return memo[(i, j)]
        
        return dp(0, 0)
                
        