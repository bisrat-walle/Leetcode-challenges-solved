class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def rec(index, opening=0):
            if index >= len(s):
                return opening == 0
            
            if opening < 0:
                return False
            
            if s[index] == "*":
                return rec(index+1, opening+1) or rec(index+1, opening-1) or rec(index+1, opening)
            elif s[index] == "(":
                return rec(index+1, opening+1)
            return rec(index+1, opening-1)
        
        return rec(0)