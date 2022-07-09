class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for i in range(n+1)]
        if n == 0:
            return 0
        nums[1] = 1
        for index in range(1, ((n-1)//2) + 1): # Some math
            nums[2*index] = nums[index]
            nums[2*index+1] = nums[index]+nums[index+1]
            
        return max(nums)
            