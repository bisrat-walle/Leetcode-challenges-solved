class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        ans = 0
        for num in nums:
            runningSum = max(0, runningSum+num, num)
            ans = max(ans, runningSum)
        
        if ans == 0:
            if 0 not in nums:
                return max(nums)
            return 0
        return ans
            