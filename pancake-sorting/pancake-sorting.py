class Solution:
    
    def flip(self, arr, k):
        for i in range(0, k//2):
            temp = arr[i]
            arr[i] = arr[k-i-1]
            arr[k-i-1] = temp
            
    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        an = []
        for i in range(len(arr), 0, -1):
            m = max(arr[:i])
            index = arr.index(m)
            self.flip(arr, index+1)
            an.append(index+1)
            self.flip(arr, i)
            an.append(i)
        return an