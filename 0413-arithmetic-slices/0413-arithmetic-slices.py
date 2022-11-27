class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 1
        ans = 0
        while right < n:
            dif = nums[right] - nums[left]
            while right+1 < n and nums[right+1] - nums[right] == dif:
                right += 1
            
            window_size = right-left+1

            if window_size > 2:
                m = window_size - 2
                number_of_subarray = (m)*(m+1)//2
                ans += number_of_subarray            
            left = right
            right += 1
        
        return ans