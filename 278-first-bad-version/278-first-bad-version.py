# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        an = self.searchBad(1, n)
        while True:
            search_result = self.searchBad(1, an-1)
            if search_result == -1:
                break
            an = search_result
        return an
        
    
    def searchBad(self, start, end):
        if start > end:
            return -1
        mid = start + (end-start)//2
        if isBadVersion(mid):
            return mid
        return self.searchBad(mid+1, end)
        
        