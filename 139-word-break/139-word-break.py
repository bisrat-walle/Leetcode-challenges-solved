class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(s):
            if not s: 
                return True

            for word in wordDict:
                if word == s[0:len(word)]:
                    if dp(s[len(word):]): return True

            return False

        return dp(s)