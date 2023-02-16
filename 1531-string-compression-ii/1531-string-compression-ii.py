class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def rec(index, k, prev, prev_count):
            if k < 0:
                return float('inf')
            if index >= n:
                return 0
            if s[index] == prev:
                return (1 if prev_count in [1, 9, 99] else 0) + \
                    rec(index+1, k, prev, prev_count+1)
            else:
                option1 = 1 + rec(index+1, k, s[index], 1) # keep
                option2 =  rec(index+1, k-1, prev, prev_count) # delete
                return min(option1, option2)
            
        return rec(0, k, "", 0)