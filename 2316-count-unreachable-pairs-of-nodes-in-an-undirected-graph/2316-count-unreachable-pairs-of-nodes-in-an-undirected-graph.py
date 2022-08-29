from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        valid = lambda i: i not in visited
        graph = defaultdict(set)
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        def dfs(i, temp_visited):
            for j in graph[i]:
                if valid(j):
                    temp_visited.add(j)
                    visited.add(j)
                    dfs(j, temp_visited)
        
        
        groups = []
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                temp_visited = {i}
                dfs(i, temp_visited)
                groups.append(len(temp_visited))
        
        total = sum(groups)
        ans = 0
        
        for i in groups:
            total -= i
            ans += i*total
        
        return ans