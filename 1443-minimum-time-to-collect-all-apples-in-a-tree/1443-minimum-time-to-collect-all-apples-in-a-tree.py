class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        self.ans = 0
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        visited = {0}
        self.apples = 0
        
        def dfs(node):
            self.apples += hasApple[node]
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    prev = self.apples
                    dfs(neighbor)
                    if prev != self.apples:
                        self.ans += 2
        
        dfs(0)
        
        return self.ans