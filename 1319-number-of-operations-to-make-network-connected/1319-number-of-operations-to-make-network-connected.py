class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        is_valid = lambda i : 0 <= i < n
        visited = set()
        
        graph = defaultdict(set)
        
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        
        def dfs(index):
            for i in graph[index]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)
        
        groups = 0
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                groups += 1
        return groups-1
            
        
        