class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        an = 0
        for i in grid:
            search_result = self.binary_search(i, 0, len(i)-1)
            # print("Negative found at", search_result, "btn", 0, len(i)-1)
            if search_result == -1:
                continue
            while True:
                temp = self.binary_search(i, 0, search_result-1)
                if temp == -1:
                    break
                search_result = temp
            
            an += len(i)-search_result
            # print("Negative at ", search_result, "for", i, "an", an)
        return an
    
    def binary_search(self, arr, left, right):
        if left > right:
            return -1
        mid = left + (right-left)//2
        # print(mid, "is mid for btn ", left, right, arr)
        if arr[mid] < 0:
            return mid
        return self.binary_search(arr, mid+1, right)
    