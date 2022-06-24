class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x: x[1])
        maxheap = []
        timeUsed = ans = 0
        
        for dur, endtime in courses:
            if (timeUsed + dur) <= endtime:
                timeUsed += dur
                heapq.heappush(maxheap, dur*-1)
                ans += 1
            else:
                if maxheap:
                    if (-1*maxheap[0]) > dur:
                        t = heapq.heappop(maxheap)*-1
                        timeUsed -= t
                        heapq.heappush(maxheap,dur*-1)
                        timeUsed += dur
        return ans