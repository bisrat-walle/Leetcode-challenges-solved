class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        di = {}
        di[0] = 1
       
        n = len(nums)
        an = 0
        s = 0
        for i in range(n):
            s += nums[i]
            if s-k in di.keys():
                an += di[s-k]
            if s in di.keys():
                di[s] += 1
            else:
                di[s] = 1
                
        return an