class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        an = 0
        nums_set = set(nums)
        for i in nums:
            if i-1 not in nums_set:
                counter = 1
                current = i
                while current+1 in nums_set:
                    current += 1
                    counter += 1
                an = max(an, counter)
        return an