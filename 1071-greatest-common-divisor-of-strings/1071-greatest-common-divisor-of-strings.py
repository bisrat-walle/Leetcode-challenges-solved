class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        n = len(str1)
        m = len(str2)
        for i in range(n):
            current = str1[:i+1]
            if n % len(current) != 0 or m % len(current) != 0:
                continue
            q1, q2 = n//len(current), m//len(current)
            if current * q1 == str1 and current * q2 == str2:
                ans = current
        return ans