class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for i in nums:
            if i in di.keys():
                di[i] += 1
            else:
                di[i] = 1
        an = []
        i = 0
        for j in sorted(di.items(), key=lambda x: x[1], reverse=True):
            
            if i >= k:
                break
            an.append(j[0])
            i += 1
        return an