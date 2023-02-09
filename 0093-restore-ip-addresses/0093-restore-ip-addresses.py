class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        ans = []
        current = []
        def rec(index):
            # print(current)
            
            if index >= len(s):
                return
            
            if len(current) == 3:
                if 0 <= int(s[index:]) <= 255 and (s[index] != "0" or s[index:] == "0"):
                    current.append(s[index:])
                    ans.append(".".join(current))
                    current.pop()
                return
            
            for n in range(1, 4):
                if 0 <= int(s[index:index+n]) <= 255 and (s[index] != "0" or s[index:index+n] == "0"):
                    current.append(s[index:index+n])
                    rec(index+n)
                    current.pop()
        
        rec(0)
        
        return ans
                    