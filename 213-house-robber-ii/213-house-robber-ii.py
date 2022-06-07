class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        @lru_cache
        def rob_safely(nums, index):
            if index >= len(nums):
                return 0
            new_money1 = rob_safely(nums, index+1)
            new_money2 = rob_safely(nums, index+2) + nums[index]
            
            return max(new_money1, new_money2)
        nums_with_first = tuple(nums[1:])
        nums_with_last = tuple(nums[:-1])  # should be hashable
        return max(rob_safely(nums_with_first, 0), rob_safely(nums_with_last, 0))