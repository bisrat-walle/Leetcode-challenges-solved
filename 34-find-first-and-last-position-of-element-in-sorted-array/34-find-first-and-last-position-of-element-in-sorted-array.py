class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ranges = []
        start, end = 0, len(nums)-1
        mid = start+(end-start)//2
        search_result = self.binary_search(nums, target, start, end)
        if search_result == -1:
            return [-1, -1]
        left, right, mid = search_result, search_result, search_result
        while True:
            
            search_result = self.binary_search(nums, target, start, mid-1)
            if search_result == -1:
                break
            left = search_result
            mid = search_result
        
        while True:
            
            search_result = self.binary_search(nums, target, mid+1, end)
            if search_result == -1:
                break
            right = search_result
            mid = search_result
        
        
        
        return [left, right]
        
    def binary_search(self, arr, val, left, right):
        if left > right:
                return -1
        mid = left + (right-left)//2
        if val == arr[mid]:
                return mid
        if val < arr[mid]:
                return self.binary_search(arr, val, left, mid-1)
        return self.binary_search(arr, val, mid+1, right)