class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        arr = []
        
        lens = len(s)
        
        if lens == 1: 
            return False
        
        if len(list(set(s))) == 1:      
            return True
        
        
        for i in range(2, lens):
            if lens%i == 0:
                arr.append(i)
        if len(arr) == 0:
            return False
        for i in range(len(arr)):
            if s[:arr[i]] * (len(s)//arr[i]) == s:
                return True
        
        return False