class Solution:
    def romanToInt(self, s: str) -> int:
        an = 0
        di = {
            'I':1,
            'V':5,
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        an += di[s[-1]]
        ln = len(s)
        special_chars = {'I':{'V', 'X'}, 'X':{'L', 'C'}, 'C':{'D', 'M'}}
        for i in reversed(range(ln-1)):
            if s[i] in special_chars and s[i+1] in special_chars[s[i]]:
                an -= di[s[i]]
            else:
                an += di[s[i]]
        
        return an