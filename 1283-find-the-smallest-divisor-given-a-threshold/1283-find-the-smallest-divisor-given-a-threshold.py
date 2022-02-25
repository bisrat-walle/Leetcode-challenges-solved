import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        
        an = 0
        
        while start <= end:
            mid = (end+start)//2
            # print(mid)
            sm = 0
            for i in nums:
                sm += math.ceil(i/mid)
            # if sm == threshold:
            #     return mid
            if sm <= threshold:
                an = mid
                end = mid - 1
            else:
                start = mid + 1
            
        return an