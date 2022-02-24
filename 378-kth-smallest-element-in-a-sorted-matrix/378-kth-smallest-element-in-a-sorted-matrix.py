from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(heap) < k:
                    heappush(heap, -1*matrix[i][j])
                else:
                    if -1*heap[0] > matrix[i][j]:
                        heappop(heap)
                        heappush(heap, -1*matrix[i][j])
        print(heap)
        return -1*heap[0]