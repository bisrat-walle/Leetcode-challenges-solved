class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for i, j ,w in times:
            graph[i].add((w, j))
        
        visited=set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited)==n:
                return travel_time
            
            for time, adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time+time, adjacent_node))
                
        return -1