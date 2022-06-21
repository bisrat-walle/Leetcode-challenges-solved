from heapq import *

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        i, j = 0, 0
        sum_ = 0
        dif_jumped_by_ladder = []
        an = 0
        
        while True:
            # print(dif_jumped_by_ladder, "an", an, "i", i, "sum", sum_)
            if i+1 == len(heights):
                # if i != 0:
                #     an += 1
                break
            if len(dif_jumped_by_ladder) < ladders:
                if heights[i+1] > heights[i]:
                    heappush(dif_jumped_by_ladder, heights[i+1] - heights[i])
                i += 1
                an += 1
                continue
            if heights[i+1] <= heights[i]:
                an += 1
                i += 1
                continue
            
            if (not dif_jumped_by_ladder) or \
                (dif_jumped_by_ladder and heights[i+1] - heights[i] <= dif_jumped_by_ladder[0]):
                sum_ += heights[i+1] - heights[i]
                if sum_ > bricks:
                    break
                an += 1
                i += 1
                    
                continue
            
            temp = heappop(dif_jumped_by_ladder)
            heappush(dif_jumped_by_ladder, heights[i+1] - heights[i])
            sum_ += temp
            if sum_ > bricks:
                break
            an += 1
            i += 1
        return an