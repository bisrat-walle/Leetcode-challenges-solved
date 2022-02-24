class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)
    
    def binary_search(self, arr, val, left, right):
        if left > right:
                return -1
        mid = left + (right-left)//2
        if val == arr[mid]:
                return mid
        if val < arr[mid]:
                return self.binary_search(arr, val, left, mid-1)
        return self.binary_search(arr, val, mid+1, right)