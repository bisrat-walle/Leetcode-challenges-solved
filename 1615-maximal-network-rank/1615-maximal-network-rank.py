class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        roadset = set((a, b) if a < b else (b, a) for a, b in roads)
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        ans = 0
        for one in range(0, n-1):
            for two in range(one + 1, n):
                val = deg[one] + deg[two]
                if (one, two) in roadset:
                    val -= 1
                ans = max(ans, val)
        return ans
                    