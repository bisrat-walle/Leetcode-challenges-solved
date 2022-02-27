class Solution:
    
    def canBeShipped(self, weights, days, mid):
        totalShipped = 0
        cannotBeShipped = False
        for wieght in weights:
            totalShipped += wieght
            if totalShipped > mid:
                days -= 1
                totalShipped = wieght
            if days == 0:
                cannotBeShipped = True
                break
        return not cannotBeShipped
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        start = max(weights)
        end = sum(weights)
        while start <= end:
            mid = start + (end-start)//2
            if self.canBeShipped(weights, days, mid):
                end = mid-1
            else:
                start = mid+1
                
        return start
        
    
        
        
    