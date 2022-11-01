class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for index in reversed(range(n-1)):
            shifts[index] += shifts[index+1]
        
        ans = [None]*n
        for index in range(n):
            ch = s[index]
            new_ascii = ord(ch)+shifts[index]
            if new_ascii > ord('z'):
                new_ascii = ord('a')+(new_ascii-ord('z')-1)%26
            ans[index] = chr(new_ascii)
        # print(ans)
        return "".join(ans)