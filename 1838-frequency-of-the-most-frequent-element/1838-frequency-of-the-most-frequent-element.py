class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 0
        left = 0
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            while left < i and sum_+k < nums[i]*(i-left+1):
                sum_ -= nums[left]
                left += 1
            max_freq = max(max_freq, i-left+1)
        return max_freq