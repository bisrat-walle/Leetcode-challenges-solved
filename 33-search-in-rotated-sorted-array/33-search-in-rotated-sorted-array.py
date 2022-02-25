class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        
        search_result = self.findPivot(nums, 0, len(nums))
        while True:
            temp = self.findPivot(nums, 0, search_result)
            if temp == -1:
                break
            search_result = temp
        
        
        if search_result == -1:
            return self.binary_search(nums, target, 0, len(nums)-1)
        
        res1 = self.binary_search(nums, target, 0, search_result-1)
        res2 = self.binary_search(nums, target, search_result, len(nums)-1)
        
        # print(search_result, res1, res2)
        
        if res1 == -1:
            return res2
        return res1
        
    def binary_search(self, arr, val, left, right):
        if left > right:
            return -1
        mid = left + (right-left)//2
        if val == arr[mid]:
            return mid
        if val < arr[mid]:
                return self.binary_search(arr, val, left, mid-1)
        return self.binary_search(arr, val, mid+1, right)
    
    def findPivot(self, arr, left, right):
        if left >= right:
            return -1
        mid = left + (right-left)//2
        if arr[0] > arr[mid]:
            return mid
        return self.findPivot(arr, mid+1, right)