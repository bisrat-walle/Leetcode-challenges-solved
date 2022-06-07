class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        memo = {}
        def is_possible(left, right):
            if right <= 0:
                return True
            if left < 0:
                return False
            if nums[left]+left >= right:
                left, right = left-1, left
            else:
                left -= 1
            return is_possible(left, right)
                
                
        
        return is_possible(len(nums)-2, len(nums)-1)