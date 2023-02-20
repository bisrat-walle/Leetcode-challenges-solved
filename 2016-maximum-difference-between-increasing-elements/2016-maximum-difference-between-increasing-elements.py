class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = nums[0]
        n = len(nums)
        ans = -1
        for i in range(n):
            ans = max(ans, nums[i]-mn)
            mn = min(mn, nums[i])
        
        return ans if ans != 0 else -1