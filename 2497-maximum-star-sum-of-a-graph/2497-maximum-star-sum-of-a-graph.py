class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = [set() for i in range(len(vals))]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        ans = float("-inf")
        
        for node in range(len(vals)):
            sor = sorted(graph[node], key=lambda k:-vals[k])
            cur = vals[node]
            n = len(sor)
            for i in range(min(n, k)):
                key = sor[i]
                if vals[key] <= 0:
                    break
                cur += vals[key]
            ans = max(ans, cur)
        
        return ans