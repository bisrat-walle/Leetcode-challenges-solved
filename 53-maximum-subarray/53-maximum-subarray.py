import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float("-inf")
        current_sum = 0
        for i in range(n):
            current_sum = max(nums[i], nums[i]+current_sum)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
            