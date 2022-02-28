class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            res = self.binary_search(i, target, 0, len(i)-1)
            if res != -1:
                return True
        return False
            
    
    def binary_search(self, arr, val, left, right):
        if left > right:
                return -1
        mid = left + (right-left)//2
        if val == arr[mid]:
                return mid
        if val < arr[mid]:
                return self.binary_search(arr, val, left, mid-1)
        return self.binary_search(arr, val, mid+1, right)