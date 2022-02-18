class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int: 
        n = len(nums)
        for i in range(n):
            if nums[i] % 2==0:
                nums[i] = 0
                continue
            nums[i] = 1
        
        prefix = [0]+[0]*n
        for i in range(n):
            prefix[i+1] = prefix[i] +  nums[i]
            
        an = 0
        di = {}
        for i in range(n+1):
            if prefix[i] - k in di.keys():
                an += di[prefix[i] - k]
            if prefix[i] in di.keys():
                di[prefix[i]] += 1
                continue
            di[prefix[i]] = 1 
        return an