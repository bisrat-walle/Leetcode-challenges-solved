class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def solve(i, j):
            if i == len(s1) and j == len(s2):
                return True
            an = False
            if i < len(s1) and s1[i] == s3[i+j]:
                an = an or solve(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                an = an or solve(i, j+1)
            return an
        
        
        return False if len(s1)+len(s2) != len(s3) else solve(0, 0)