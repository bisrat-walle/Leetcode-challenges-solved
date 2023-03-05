class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def isThereAtLeastKPairs(mid):
            total = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                total += right - left
            
            return total >= k
        
        nums.sort()
        
        left, right = 0, max(nums) - min(nums)
        while left < right:
            mid = (left+right)//2
            if isThereAtLeastKPairs(mid):
                right = mid
            else:
                left = mid+1
        
        return left
        