import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for i in nums:
            if i in di.keys():
                di[i] += 1
            else:
                di[i] = 1
            
        return heapq.nlargest(k, di.keys(), key=lambda k:di[k])