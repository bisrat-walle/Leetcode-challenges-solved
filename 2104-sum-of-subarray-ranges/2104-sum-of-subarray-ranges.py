class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        an = 0
        for i, j in enumerate(nums):
            min_ = j
            max_ = j
            for k in range(i+1, len(nums)):
                min_ = min(min_, nums[k])
                max_ = max(max_, nums[k])
                an += max_-min_
        return an