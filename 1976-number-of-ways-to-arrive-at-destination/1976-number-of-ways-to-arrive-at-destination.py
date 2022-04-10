from collections import defaultdict
from heapq import *

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[v].append((u, time))
            graph[u].append((v, time))
        
        times = [float("inf") for i in range(n)]
        times[0] = 0
        ways = [0 for i in range(n)]
        ways[0] = 1
        heap = [(0, 0)]
        
        while heap:
            last_time, u = heappop(heap)
            
            for v, time in graph[u]:
                new_time = last_time + time
                if new_time < times[v]:
                    heappush(heap, (new_time, v))
                    times[v] = new_time
                    ways[v] = ways[u]
                elif new_time == times[v]:
                    ways[v] += ways[u]
        # print(ways, times)
        return ways[-1] % (10**9 + 7)