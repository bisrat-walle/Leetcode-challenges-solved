class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        con = set(map(tuple, connections))
        
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        
        an = 0
        visited = set()
        visited.add(0)
        def dfs(i=0):
            nonlocal an
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    if (j, i) not in con:
                        an += 1
                    dfs(j)
        dfs()
        return an