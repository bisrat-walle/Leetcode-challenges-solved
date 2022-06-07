from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        rev_graph = defaultdict(set)
        
        for start, end in edges:
            rev_graph[end].add(start)
        
        def dfs(i, visited):
            visited.add(i)
            for j in rev_graph[i]:
                if j not in visited:
                    dfs(j, visited)
        
        an = []
        
        for i in range(n):
            current_visited = set()
            dfs(i, current_visited)
            current_visited.discard(i)
            an.append(list(sorted(current_visited)))
        
        return an
        
        