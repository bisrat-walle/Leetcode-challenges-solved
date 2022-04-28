import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum < 0:
                pre_sum = 0
            pre_sum += nums[i]
            max_sum = max(pre_sum, max_sum)
            
        return max_sum
            