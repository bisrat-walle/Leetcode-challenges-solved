from collections import defaultdict
from heapq import *

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inDegrees = [0 for i in range(n)]
        outgoing = defaultdict(set)
        for pre, course in relations:
            inDegrees[course-1] += 1
            outgoing[pre-1].add(course-1)
        
        heap = []
        for course in range(n):
            if inDegrees[course] == 0:
                heappush(heap, (time[course], course))
        an = 0
        while heap:
            tim, course = heappop(heap)
            an = tim
            for neigh in outgoing[course]:
                inDegrees[neigh] -= 1
                if inDegrees[neigh] == 0:
                    heappush(heap, (time[neigh]+tim, neigh))
        return an