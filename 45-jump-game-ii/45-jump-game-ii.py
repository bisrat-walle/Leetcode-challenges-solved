class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for i in range(len(nums))]
        dp[len(nums)-1] = 0
        for i in reversed(range(0, len(nums)-1)):
            for j in range(nums[i], 0, -1):
                temp = i+j
                if temp > len(nums)-1:
                    temp = len(nums)-1
                dp[i] = min(dp[i], 1+dp[temp])
        
        
        return dp[0]