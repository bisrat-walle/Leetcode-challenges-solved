class Solution:
    def minPairSum(self, nums: List[int]) -> int():
        nums.sort()
        n = len(nums)
        sums = []
        for i in range(n//2):
            sums.append(nums[i]+nums[n-i-1])
        return max(sums)