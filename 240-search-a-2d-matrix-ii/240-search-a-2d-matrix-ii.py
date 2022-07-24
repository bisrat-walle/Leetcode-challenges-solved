class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left+right)//2
                if arr[mid] < target:
                    left = mid+ 1
                else:
                    right = mid
            if arr[right] == target:
                return True

        return False