class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if target == source:
            return 0
        
        
        graph = defaultdict(set)
        routes = list(map(set, routes))
        queue = deque()
        endings = set()
        visited = set()
        
        for i, route in enumerate(routes):
            
            if source in route:
                queue.append((i, 1))
                visited.add((i, 1))
                
            if target in route:
                endings.add(i)
            
            for j in range(i+1, len(routes)):
                if route & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)
                    
        
        while queue:
            current, cnt = queue.popleft()
            if current in endings:
                return cnt
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cnt+1))
        
        return -1
        