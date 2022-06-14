class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(n):
            if n == 1:
                return "1"
            prev = rec(n-1)
            an = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    an += f"{count}{prev[i-1]}"
                    count = 1
                    
            an += f"{count}{prev[-1]}"
            return an
        return rec(n)