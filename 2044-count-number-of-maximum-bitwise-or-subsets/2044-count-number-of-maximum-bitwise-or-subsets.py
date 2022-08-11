class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        ans = 0
        
        for mask in range(1<<len(nums)):
            current = 0
            for bit in range(len(nums)-1, -1, -1):
                if mask & 1<<bit:
                    current |= nums[bit]
            if current == max_or:
                ans += 1
        
        return ans