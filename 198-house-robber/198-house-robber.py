class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob_safely(index):
            if index >= len(nums):
                return 0
            new_money1 = rob_safely(index+1)
            new_money2 = rob_safely(index+2) + nums[index]
            
            return max(new_money1, new_money2)
        return rob_safely(0)