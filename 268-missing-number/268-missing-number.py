class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        su_ = n*(n+1)//2
        return su_ - sum(nums)