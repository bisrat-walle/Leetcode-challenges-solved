from heapq import *
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        current_day = 1
        counter = Counter(tasks)
        heap = []
        queue = deque()
        
        for count in counter.values():
            heappush(heap, -1 * count) # max heap
            
        while heap or queue:
            if heap:
                count = -1*heappop(heap)
                if count-1 != 0:
                    queue.append((current_day+n, count-1))
            if queue and queue[0][0] == current_day:
                heappush(heap, -1*queue.popleft()[1])
            current_day += 1
        
        return current_day - 1