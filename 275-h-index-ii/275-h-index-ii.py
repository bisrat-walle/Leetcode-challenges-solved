class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n
        while left < right:
            mid = left + (right-left)//2
            if citations[mid] < n - mid: 
                left = mid + 1
            else:
                right = mid
        return n - left
