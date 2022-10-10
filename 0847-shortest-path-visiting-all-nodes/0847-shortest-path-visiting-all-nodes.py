class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        level = 0
        n = len(graph)
        queue = deque([(i, 1<<i) for i in range(n)])
        visited = {(i, 1<<i) for i in range(n)}
        while queue:
            for _ in range(len(queue)):
                node, vis = queue.popleft()
                if vis == 2**n-1:
                    return level
                # print(graph)
                for neigh in graph[node]:
                    if (neigh, vis|(1<<neigh)) not in visited:
                        visited.add((neigh, vis|(1<<neigh)))
                        queue.append((neigh, vis|(1<<neigh)))
                
            level += 1
        
        