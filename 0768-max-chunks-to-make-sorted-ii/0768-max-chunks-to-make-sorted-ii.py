class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        sorted_arr = sorted(arr)
        chunks = 0
        for index in range(n):
            if sorted(arr[:index+1]) == sorted_arr[:index+1]:
                chunks += 1
            
        return chunks