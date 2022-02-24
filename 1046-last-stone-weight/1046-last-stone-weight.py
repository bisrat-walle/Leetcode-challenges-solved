from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapify(stones)
        while True:
            # print(stones)
            if len(stones) < 2:
                break
            heavy1 = -1*heappop(stones)
            heavy2 = -1*heappop(stones)
            if heavy1 == heavy2:
                continue
            heappush(stones, -1*(heavy1-heavy2))
        if len(stones) == 0:
            return 0
        return -1*stones[0]
            
            