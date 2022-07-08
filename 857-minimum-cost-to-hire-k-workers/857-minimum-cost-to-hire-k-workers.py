from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        criteria = sorted((w/q, q, w) for q, w in zip(quality, wage))

        ans = float('inf')
        heap = []
        quality_sum = 0
        for ratio, quality, _ in criteria:
            
            heappush(heap, -quality)
            quality_sum += quality

            if len(heap) > k:
                quality_sum += heappop(heap) # Since it is negative

            if len(heap) == k:
                ans = min(ans, ratio * quality_sum)

        return float(ans)