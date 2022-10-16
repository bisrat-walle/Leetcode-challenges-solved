class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums) 
        outOfBound = lambda right: nums[right] < minK or nums[right] > maxK
        valid = lambda left, current_max, current_min:left < current_max and left < current_min
        current_min, current_max = -1, -1
        left = -1

        ans = 0        
        for right in range(n):
            if outOfBound(right): 
                left = right
                continue               
            current_min = right if nums[right] == minK else current_min
            current_max = right if nums[right] == maxK else current_max
                
            if valid(left, current_max, current_min):
                ans += (min(current_max, current_min) - left)
                            
        return ans