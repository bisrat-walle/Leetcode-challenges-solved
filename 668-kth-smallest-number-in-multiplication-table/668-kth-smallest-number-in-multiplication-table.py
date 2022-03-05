class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def hasPotential(mid):
            counter = 0
            for i in range(1, m+1):
                counter += min(mid//i, n)
            return counter >= k
        
        start, end = 1, m*n
        while start < end:
            mid = start + (end-start)//2
            if hasPotential(mid):
                end = mid
            else:
                start = mid+1
        return start
        
        
        
        