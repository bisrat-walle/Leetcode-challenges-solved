class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        first, second, third = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > third:
                first, second, third = second, third, num
            elif num > second:
                first, second = second, num
            elif num > first:
                first = num
        
        return first