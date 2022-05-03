class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float("-inf")
        current_sum = 0
        for i in range(n):
            current_sum = max(nums[i], nums[i]+current_sum)
            max_sum = max(max_sum, current_sum)
        
        rightsums = [None] * n
        rightsums[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            rightsums[i] = rightsums[i+1] + nums[i]

        
        maxright = [None] * n
        maxright[-1] = rightsums[-1]
        for i in range(n-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])

        leftsum = 0
        for i in range(n-2):
            leftsum += nums[i]
            max_sum = max(max_sum, leftsum + maxright[i+2])
        return max_sum
            