class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = {}
        start = 0
        max_length = 0
            
        for end, c in enumerate(s):
            if c in di:
                start = max(start, di[c] + 1)
            
            max_length = max(max_length, end - start + 1)
            di[c] = end
        return max_length
                
        