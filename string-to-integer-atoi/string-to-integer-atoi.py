class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        try:
            int(s[0])
        except ValueError:
            if not(s[0] == ' ' or s[0] == '-' or s[0] == '+'):
               return 0
        negative = None
        if s[0] == '+':
            negative = False
        if s[0] == '-':
            negative = True
        start = 0
        end = 0
        if negative != None:
            start = 1
        
        
        for i in range(start, len(s)):
            try:
                int(s[i:i+1])
            except ValueError:
                end = i
                break
            end = len(s)
        try:
            if int(s[start:end])>=(2**31-1) and not negative:
                return 2**31-1
            
            if negative == None:
                return int(s[start:end])

            if negative:
                if int(s[start:end]) > 2**31:
                    return -1*2**31
                return -1 * int(s[start:end])
               
            return int(s[start:end])
            
        except ValueError:
            return 0
            