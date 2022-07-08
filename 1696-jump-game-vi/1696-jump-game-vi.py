from heapq import *


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        heap = []
        heappush(heap, (-nums[0], 0))
        for i in range(1, len(nums) - 1):
            while heap[0][1] < i - k:
                heappop(heap)
            
            heappush(heap, (- (nums[i] - heap[0][0]), i))
        
        if heap[0][1] < len(nums) - 1 - k:
            heappop(heap)
        return - heap[0][0] + nums[-1]
            