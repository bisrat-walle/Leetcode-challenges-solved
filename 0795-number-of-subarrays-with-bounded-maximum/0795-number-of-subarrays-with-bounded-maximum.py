class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def getSubstringsWithMaxAtmostK(k):
            n = len(nums)
            res = 0
            left = 0
            for right in range(n):
                if nums[right] > k:
                    left = right+1
                    continue
                res += right-left+1
            return res
        
        
        
        return getSubstringsWithMaxAtmostK(right) - getSubstringsWithMaxAtmostK(left-1)