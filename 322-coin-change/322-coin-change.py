class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def rec(current):
            if current in cache:
                return cache[current]
            if current < 0:
                return float("inf")
            if current == 0:
                return 0
            ans = float("inf")
            for coin in coins:
                ans = min(ans, 1+rec(current-coin))
            cache[current] = ans
            return cache[current]
        
        res = rec(amount)
        return -1 if res == float("inf") else res
            