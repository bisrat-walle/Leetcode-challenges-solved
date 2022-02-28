class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if totalTrips == 1:
            return min(time)
        
        left, right = 1, sum(time) * totalTrips
        
        while left < right:
            mid = left + (right-left)//2
            if self.checkTimes(time, mid, totalTrips):
                right = mid
            else:
                left = mid+1
        
        return left
    
    
    def checkTimes(self, time, mid, totalTrips):
        total = 0
        for i in time:
            total += mid//i
        
        # print("Completed at ", mid, total)
        
        return total >= totalTrips