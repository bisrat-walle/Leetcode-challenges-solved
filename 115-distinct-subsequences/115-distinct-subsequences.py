class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def rec(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            ans = rec(i+1, j)
            if s[i] == t[j]:
                ans += rec(i+1, j+1)
            return ans
        return rec(0, 0)
        