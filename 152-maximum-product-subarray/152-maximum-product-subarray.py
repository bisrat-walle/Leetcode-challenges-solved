class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Kadane's Algorithm is important BW
        
        cur_max, cur_min, global_max = 1, 1, max(nums)
        for num in nums:
            cur_max_cp = cur_max
            cur_max = max(cur_max*num, cur_min*num, num)
            cur_min = min(cur_max_cp*num, cur_min*num, num)
            global_max = max(global_max, cur_max)
        return global_max