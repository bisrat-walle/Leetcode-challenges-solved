class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        an = []
        n = len(nums)
        for i in range(n):
            c = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    c += 1
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    c += 1
            an.append(c)
        return an
                
            
        