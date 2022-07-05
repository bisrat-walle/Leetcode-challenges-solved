class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        an = 0
        for num in nums:
            if num-1 not in nums_set:
                current = num
                current_an = 1
                
                while current+1 in nums_set:
                    current += 1
                    current_an += 1
                    
                an = max(an, current_an)
        return an