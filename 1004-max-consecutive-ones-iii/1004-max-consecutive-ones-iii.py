class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        an = float("-inf")
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
                
            an = max(an, j-i+1)
            j += 1
        return an
                